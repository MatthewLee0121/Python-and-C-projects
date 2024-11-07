#include <pybind11/pybind11.h>
#include <sqlite3.h>

int connect_to_db() {
    sqlite3 *db;
    int rc = sqlite3_open("example.db", &db);
    if(rc) {
        sqlite3_close(db);
        return 1; // Failed to open database
    }
    sqlite3_close(db);
    return 0; // Success
}

PYBIND11_MODULE(my_backend, m) {
    m.def("connect_to_db", &connect_to_db, "A function that connects to the database");
}
