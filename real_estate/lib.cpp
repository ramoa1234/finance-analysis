#include <stdio.h>
#include <iostream>


extern "C" {
    void hello() {
        std::cout << "hello, world" << std::endl;
    }
}