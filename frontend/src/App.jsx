import { useState } from "react";
import {
  Send,
  Plane,
  Map,
  Hotel,
  CloudSun,
  Wallet,
  Loader2,
} from "lucide-react";

import {
  sendTravelQuery,
  generateItinerary,
  uploadTravelPDF,
  askRAGQuestion,
} from "./api";
import "./App.css";

function App() {
  const [message, setMessage] = useState("");
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);

  const [destination, setDestination] = useState("");
  const [days, setDays] = useState(3);
  const [interests, setInterests] = useState("");

  const [itinerary, setItinerary] = useState("");
  const [itineraryLoading, setItineraryLoading] = useState(false);

  

  const [ragFile, setRagFile] = useState(null);
  const [ragQuestion, setRagQuestion] = useState("");
  const [ragAnswer, setRagAnswer] = useState("");
  const [ragLoading, setRagLoading] = useState(false);
  const [ragUploading, setRagUploading] = useState(false);
  const [ragMessage, setRagMessage] = useState("");

  const handleSend = async () => {
    if (!message.trim() || loading) return;

    const userMessage = message.trim();

    setMessages((previous) => [
      ...previous,
      { role: "user", content: userMessage },
    ]);

    setMessage("");
    setLoading(true);

    try {
      const result = await sendTravelQuery(userMessage);

      setMessages((previous) => [
        ...previous,
        {
          role: "assistant",
          content:
            result.answer || "I couldn't generate a response.",
        },
      ]);
    } catch (error) {
      setMessages((previous) => [
        ...previous,
        {
          role: "assistant",
          content:
            "Unable to connect to the travel assistant. Please make sure the backend is running.",
        },
      ]);
    } finally {
      setLoading(false);
    }
  };

  const handleItinerary = async () => {
    if (!destination.trim() || itineraryLoading) return;

    setItineraryLoading(true);
    setItinerary("");

    try {
      const result = await generateItinerary(
        destination,
        Number(days),
        interests || "general sightseeing"
      );

      setItinerary(
        result.itinerary || result.message || "No itinerary generated."
      );
    } catch (error) {
      setItinerary(
        "Unable to generate the itinerary. Please make sure the backend is running."
      );
    } finally {
      setItineraryLoading(false);
    }
  };
    const handleRAGUpload = async () => {
    if (!ragFile || ragUploading) return;

    setRagUploading(true);
    setRagMessage("");
    setRagAnswer("");

    try {
      const result = await uploadTravelPDF(ragFile);

      if (result.success) {
        setRagMessage(
          `${result.filename} uploaded successfully. ${result.chunks} text chunks created.`
        );
      } else {
        setRagMessage(result.message || "PDF upload failed.");
      }
    } catch (error) {
      setRagMessage(
        "Unable to upload the PDF. Please make sure the backend is running."
      );
    } finally {
      setRagUploading(false);
    }
  };

  const handleRAGQuestion = async () => {
    if (!ragQuestion.trim() || ragLoading) return;

    setRagLoading(true);
    setRagAnswer("");

    try {
      const result = await askRAGQuestion(ragQuestion);

      setRagAnswer(
        result.answer || "No answer was generated from the document."
      );
    } catch (error) {
      setRagAnswer(
        "Unable to query the document. Please make sure a PDF has been uploaded."
      );
    } finally {
      setRagLoading(false);
    }
  };

  return (
    <div className="app">
      <header className="navbar">
        <div className="brand">
          <div className="brand-icon">
            <Plane size={22} />
          </div>

          <div>
            <h1>TravelAI</h1>
            <span>AI Travel Concierge</span>
          </div>
        </div>

        <div className="status">
          <span className="status-dot"></span>
          AI Concierge Online
        </div>
      </header>

      <main className="container">
        <section className="hero">
          <p className="eyebrow">YOUR PERSONAL AI TRAVEL ASSISTANT</p>

          <h2>
            Plan smarter.
            <br />
            <span>Travel better.</span>
          </h2>

          <p className="hero-text">
            Ask about destinations, weather, hotels, currencies,
            attractions, and personalized itineraries.
          </p>
        </section>

        <section className="feature-grid">
          <div className="feature-card">
            <CloudSun size={24} />
            <h3>Weather</h3>
            <p>Get current weather information for your destination.</p>
          </div>

          <div className="feature-card">
            <Hotel size={24} />
            <h3>Hotels</h3>
            <p>Search accommodation options for your trip.</p>
          </div>

          <div className="feature-card">
            <Wallet size={24} />
            <h3>Currency</h3>
            <p>Convert currencies using current exchange rates.</p>
          </div>

          <div className="feature-card">
            <Map size={24} />
            <h3>Travel Info</h3>
            <p>Discover attractions and useful travel information.</p>
          </div>
        </section>

        <section className="chat-section">
          <div className="section-heading">
            <div>
              <p className="eyebrow">AI CONCIERGE</p>
              <h2>Ask anything about your trip</h2>
            </div>
          </div>

          <div className="chat-box">
            <div className="messages">
              {messages.length === 0 && (
                <div className="empty-chat">
                  <Plane size={38} />
                  <h3>Where would you like to go?</h3>
                  <p>
                    Try asking:
                    <br />
                    "What's the weather in Hyderabad?"
                    <br />
                    "Find hotels in Goa"
                    <br />
                    "Convert 100 USD to INR"
                  </p>
                </div>
              )}

              {messages.map((item, index) => (
                <div
                  key={index}
                  className={`message ${
                    item.role === "user" ? "user-message" : "ai-message"
                  }`}
                >
                  <div className="message-label">
                    {item.role === "user" ? "You" : "TravelAI"}
                  </div>

                  <div className="message-content">
                    {item.content}
                  </div>
                </div>
              ))}

              {loading && (
                <div className="message ai-message">
                  <div className="message-label">TravelAI</div>

                  <div className="message-content loading">
                    <Loader2 className="spinner" size={18} />
                    Thinking...
                  </div>
                </div>
              )}
            </div>

            <div className="input-area">
              <input
                value={message}
                onChange={(event) => setMessage(event.target.value)}
                onKeyDown={(event) => {
                  if (event.key === "Enter") {
                    handleSend();
                  }
                }}
                placeholder="Ask your travel assistant..."
              />

              <button
                onClick={handleSend}
                disabled={loading || !message.trim()}
              >
                <Send size={18} />
              </button>
            </div>
          </div>
        </section>

        <section className="itinerary-section">
          <div className="section-heading">
            <div>
              <p className="eyebrow">SMART PLANNING</p>
              <h2>Build your itinerary</h2>
            </div>
          </div>

          <div className="itinerary-card">
            <div className="form-grid">
              <div className="form-group">
                <label>Destination</label>

                <input
                  value={destination}
                  onChange={(event) =>
                    setDestination(event.target.value)
                  }
                  placeholder="e.g. Hyderabad"
                />
              </div>

              <div className="form-group">
                <label>Days</label>

                <input
                  type="number"
                  min="1"
                  max="30"
                  value={days}
                  onChange={(event) => setDays(event.target.value)}
                />
              </div>

              <div className="form-group full-width">
                <label>Interests</label>

                <input
                  value={interests}
                  onChange={(event) =>
                    setInterests(event.target.value)
                  }
                  placeholder="e.g. food, history, beaches"
                />
              </div>
            </div>

            <button
              className="primary-button"
              onClick={handleItinerary}
              disabled={itineraryLoading || !destination.trim()}
            >
              {itineraryLoading ? (
                <>
                  <Loader2 className="spinner" size={18} />
                  Creating itinerary...
                </>
              ) : (
                <>
                  <Map size={18} />
                  Generate Itinerary
                </>
              )}
            </button>

            {itinerary && (
              <div className="itinerary-result">
                <h3>Your personalized itinerary</h3>

                <div className="itinerary-content">
                  {itinerary}
                </div>
              </div>
            )}
          </div>
        </section>
                <section className="rag-section">
          <div className="section-heading">
            <div>
              <p className="eyebrow">DOCUMENT INTELLIGENCE</p>
              <h2>Chat with your travel document</h2>
            </div>
          </div>

          <div className="rag-card">
            <div className="rag-upload">
              <label className="form-group">
                <span>Upload Travel PDF</span>

                <input
                  type="file"
                  accept=".pdf"
                  onChange={(event) =>
                    setRagFile(event.target.files[0] || null)
                  }
                />
              </label>

              <button
                className="primary-button"
                onClick={handleRAGUpload}
                disabled={ragUploading || !ragFile}
              >
                {ragUploading ? (
                  <>
                    <Loader2 className="spinner" size={18} />
                    Processing PDF...
                  </>
                ) : (
                  "Upload PDF"
                )}
              </button>
            </div>

            {ragMessage && (
              <div className="rag-message">
                {ragMessage}
              </div>
            )}

            <div className="rag-question">
              <label>Ask about your document</label>

              <div className="rag-input-row">
                <input
                  value={ragQuestion}
                  onChange={(event) =>
                    setRagQuestion(event.target.value)
                  }
                  onKeyDown={(event) => {
                    if (event.key === "Enter") {
                      handleRAGQuestion();
                    }
                  }}
                  placeholder="e.g. What are the recommended hotels?"
                />

                <button
                  onClick={handleRAGQuestion}
                  disabled={ragLoading || !ragQuestion.trim()}
                >
                  {ragLoading ? (
                    <Loader2 className="spinner" size={18} />
                  ) : (
                    <Send size={18} />
                  )}
                </button>
              </div>
            </div>

            {ragAnswer && (
              <div className="rag-result">
                <h3>Document Answer</h3>
                <p>{ragAnswer}</p>
              </div>
            )}
          </div>
        </section>
      </main>

      <footer>
        <p>
          TravelAI • Powered by LangGraph, Gemini &amp; FastAPI
        </p>
      </footer>
    </div>
  );
}

export default App;