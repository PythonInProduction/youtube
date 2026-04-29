#include <format>
#include <map>
#include <stdexcept>
#include <string>
#include <unordered_set>
#include <vector>
#include "validate.hpp"

// Entity
using Guest = int;

// Component
using Name = std::string;

// World
class RestaurantBar {
public:
    std::map<Guest, Name> names;
    std::unordered_set<Guest> drinkers;

    void parse_guest(const std::string& name, const std::string& raw_age) {
        int age = std::stoi(raw_age);
        if (!is_valid(age, 18)) {
            throw std::invalid_argument(std::format("Guest {} is underage: {}", name, age));
        }
        Guest guest = admit(name);
        if (is_valid(age, 21)) {
            drinkers.insert(guest);
        }
    }

private:
    int id = 0;

    Guest admit(const std::string& name) {
        Guest guest = id++;
        names[guest] = name;
        return guest;
    }
};

// System
std::vector<std::string> serve_food(const RestaurantBar& world) {
    std::vector<std::string> orders;
    for (const auto& [guest, name] : world.names) {
        orders.push_back(std::format("Ribeye for {}", name));
    }
    return orders;
}

std::vector<std::string> serve_drink(const RestaurantBar& world) {
    std::vector<std::string> orders;
    for (const Guest& guest : world.drinkers) {
        orders.push_back(std::format("Wine for {}", world.names.at(guest)));
    }
    return orders;
}
