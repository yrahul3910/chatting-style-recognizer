#include <iostream>
#include <fstream>
#include <string>
#include <cstring>

using namespace std;
int main(int argc, char** argv) {
	if (argc != 4) {
		cout << "Arguments invalid.Format:\n"
			<< "segregate <input file> <name1> <name2>";
	}

	ifstream fin(argv[0]);
	ofstream fout1("1.txt");
	ofstream fout2("2.txt");
	while(!fin.eof()) {
		string x;
		getline(fin, x);

		/* Must parse each line in the exported WhatsApp
		log. This might differ in different versions of
		WhatsApp. */
		int pos;
		pos = x.find(',');
		x = x.substr(pos+1);
		pos = x.find('-');
		x = x.substr(pos + 1);

		char ch = x[3];
		x = x.substr(x.find(':')+2);
		/* In the below else if conditions, argv[1] and argv[2]
		are the names of the people as given in the WhatsApp
		chat history. The second index given will vary and is the
		first index of the name string at which the characters vary.
		For example, if the names are John and Josh, then the second
		index would be 2. */
		if(ch == argv[1][0])
            fout1 << x << endl;
       	else if(ch == argv[2][0])
        	fout2 << x << endl;
	}
	fin.close();
	fout1.close();
	fout2.close();
}

