from database.db import (
    create_tables,
    save_search,
    get_search_history
)


print("----- DATABASE TEST -----")

create_tables()

save_search(
    search_type="hotel",
    destination="Goa",
    check_in="2026-10-10",
    check_out="2026-10-12",
    adults=2,
    query="Find hotels in Goa"
)

history = get_search_history()

for row in history:
    print(row)