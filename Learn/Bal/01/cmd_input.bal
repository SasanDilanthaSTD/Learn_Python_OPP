import ballerina/io;

public function main(int val) returns error? {
    io:println(val);

    if val >=0 {
        return error("Invalied input");
    }
}