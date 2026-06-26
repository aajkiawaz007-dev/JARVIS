# =====================================================
# UNIVERSAL DATABASE ADAPTER
# =====================================================

from backend import (
    load_data,
    save_data
)


class DatabaseAdapter:

    def read(self):

        return load_data()


    def write(self, data):

        save_data(data)

        return True


    def update(self, key, value):

        data = load_data()

        data[key] = value

        save_data(data)

        return True


    def delete(self, key):

        data = load_data()

        if key in data:

            del data[key]

            save_data(data)

        return True