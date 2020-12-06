

#include <iostream>
#include <fstream>
#include "option.h"
#include <vector>
int main(int argc, char ** argv){
 OptionParser op(argc, argv);
	if (!op.validCheck()){
		printf("Parameters error, please check the readme.txt file for correct format!\n");
		return -1;
	}
	char * inFile = op.getPara("-i");
	if (inFile == NULL){
		inFile = (char*)"network.cost";
	}

	std::vector<int> costs;
	costs.push_back(-1);
    std::fstream f;
	f.open(inFile, std::ios::in);
    if(!f){
    std::cout<<"err";
    return 1;
    }
	while (!f.eof())
	{
	int n;
		f >> n;
		//std::cout<<n<<std::endl;
		costs.push_back(n);
	}

	f.close();
    costs.pop_back();
    std::cout<<"amout of node "<<costs.size()-1<<std::endl;

    std::fstream out("result.txt",std::ios::out);
    if(!out){
    std::cout<<"ree";
    return 1;
    }

	for (unsigned int i = costs.size()-10; i < costs.size(); ++i){
        std::cout<< costs.at(i)<<std::endl;
        //out<<costs.at(i)<<std::endl;

	}
   // out.close();


	return 0;

}
