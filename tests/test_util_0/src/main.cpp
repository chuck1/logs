#include <cassert>
#include <iostream>

#include <util/thread_for.hpp>

int main(int ac, char ** av)
{

	int n = atoi(av[1]);

	std::vector<unsigned int> v(1E8);
	unsigned int c = 0;
	for(auto && i : v) {
		i = c++;
	}
	
	util::thread_for<typename std::vector<unsigned int>::iterator, unsigned int &>(v.begin(), v.end(), [](unsigned int & i) { i %= 13; }, n);
	
	for(auto && i : v) {
		//std::cout << i << " ";
	}
	//std::cout << std::endl;
}

