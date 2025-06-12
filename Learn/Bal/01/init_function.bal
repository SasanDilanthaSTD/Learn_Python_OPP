import ballerina/io;

// create uninitalize variable
int val;
// create uninitialized final variable
final string name;

function init() returns error? {
    // set valuses
    val = 2;
    name = "Sasan";

    if val >= 3{
        return error("value should be less than 3");
    }
}

public function main() {
    io:print(name);
}