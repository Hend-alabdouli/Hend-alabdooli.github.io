//============================================================================
// Name         : lab3.cpp
// Author       : Khalid Mengal
// Version      : 1.0
// Date Created : 22-09-2020
// Date Modified: 02-01-2021 
// Description  : Singly Linked-List implementation in C++
//============================================================================
#include<iostream>
#include<string>
#include<fstream>
#include<exception>
#include<sstream>
using namespace std;
//====================================
class Node
{
	private:
		int elem; //data element 
		Node* next; //Link (pointer) to the next Node
		
	public:
		Node(int elem) : elem(elem), next(NULL)
		{}
		friend class MyLinkedList ;
};
//=====================================
class MyLinkedList
{
	private:
		Node* head; // pointer to the head of list
	public:
		MyLinkedList (); // empty list constructor
		~MyLinkedList (); // destructor to clean up all nodes
		bool empty() const; // is list empty?
		void addFront(int elem); // add a new Node at the front of the list
		void removeFront(); // remove front Node from the list
		unsigned int countElem(int elem); //count frequency of an element in the list
		int getIndexOf(int elem); //returns first index of an element in the list, -1 if the element is not present
		void display() const;
		void loadData(string); //read a file and load it into the linked list
		void dumpData(string) const; //write the linked list to a file
		void sort();  // sort the elements of the list
};
//=====================================
void listCommands()
{
	cout<<"List of available Commands:"<<endl
		<<"display            : Display the Linked List"<<endl
		<<"addFront <element> : Add <element> to the front of the Linked List"<<endl
		<<"removeFront        : Remove the front node of the Linked List"<<endl
		<<"count              : count frequency of an element in the list"<<endl
		<<"indexOf            : return first index of an elemenent in the list (-1 of not present)"<<endl
		<<"load <file_name>   : Load the data from <file> and add it into the Linked List"<<endl
		<<"dump <file_name>   : Dump the contents of the Linked list to <file>"<<endl
		<<"sort               : Sort the Linked List using Bubble Sort Algorithm"<<endl
		<<"help               : Display the list of available commands"<<endl
		<<"exit               : Exit the Program"<<endl;
}
//=======================================
// main function
int main()
{

	MyLinkedList myList;

	listCommands();
	string user_input;
	string command;
	string parameter;

	do
	{
		cout<<">";
		getline(cin,user_input);
		
		// parse userinput into command and parameter(s)
		stringstream sstr(user_input);
		getline(sstr,command,' ');
		getline(sstr,parameter);
		
		
		if(command=="display") 				myList.display();
		else if(command=="addFront" or command=="add")				myList.addFront(stoi(parameter)),myList.display();
		else if(command=="removeFront" or command=="remove")		myList.removeFront(),myList.display();
		else if(command=="count")			cout<<parameter<<" occurs "<<myList.countElem(stoi(parameter))<<" time(s) in the list"<<endl;
		else if(command=="indexOf")         cout<<"First index of "<<parameter<<" in the list is: "<<myList.getIndexOf(stoi(parameter))<<endl;
		else if(command=="load")			myList.loadData(parameter),myList.display();
		else if(command == "dump")			myList.dumpData(parameter);
		else if(command == "sort")			myList.sort(),myList.display();
		else if(command == "help")			listCommands();
		else if(command == "exit")			break;
		else 								cout<<"Invalid Commad !!"<<endl;
	}while(command!="exit");

	return EXIT_SUCCESS;
}
//====================================
// constructor
MyLinkedList::MyLinkedList ()
{
	this->head = NULL;
}
//====================================
// destructor to clean up all nodes
MyLinkedList::~MyLinkedList () 
{
	while (!empty()) removeFront();
	//todo
}
//====================================
// Check if the list is empty or not
bool MyLinkedList::empty() const 
{
	return head == NULL;
	//todo
}
//====================================
// add a node at the front of the list
void MyLinkedList::addFront(int elem)
{
	Node* newnode = new Node(elem); 
	newnode->elem = elem; 
	newnode->next = head; 
	head = newnode; 
	//todo
}
//====================================
// remove the first node from the list
void MyLinkedList::removeFront()
{
	Node* old = head; 
	head = old->next; 
	delete old;
	//todo

}
//====================================
// count frequency of an element in the list
unsigned int MyLinkedList::countElem(int elem)
{ 
	Node* current=head;
	int count=0;
	while (current!= NULL){
		if(current->elem==elem)
			count++;
		current=current->next;
	}
	return count;
	//todo
}
//==============================================
// get first index of an element in the the list.
// returns -1 if the element is not present
int MyLinkedList::getIndexOf(int elem)
{
	Node* current=head;
	int index=0;
	while (current!= NULL){
		if(current->elem==elem)
			return index;
		current=current->next;
		index++;
	}
	return -1;
	//todo
}
//==============================================
// display all nodes of the linked list
void MyLinkedList::display() const
{	Node* current=head;
	if(current==NULL){
		cout<<" List is empty"<<endl;
	}
	else{
		cout<<"Head";
		while (current!=NULL){
			cout<<"->"<<current->elem;
			current=current->next;
		}
		cout<<"->"<<"Null"<<endl;
	}
	//todo
}
//====================================
// sort the elments of the list using bubble_sort
void MyLinkedList::sort()
{	Node* temp=head;
	int len=0;
	while (temp!= NULL){
		len++;
		temp=temp->next;
	}
	int swapped, i,j,value;
	Node* current;
	Node* pointer1;
	Node* pointer2;
	
	for(i=0;i<len-1;i++){
		swapped=0;
		current=head;
		for(j=0;j<len-i-1;j++){
			pointer1=current;
			pointer2=pointer1->next;
			if(pointer1->elem>pointer2->elem){
				value=pointer1->elem;
				pointer1->elem=pointer2->elem;
				pointer2->elem=value;
				swapped=1;
			}
			current=current->next;

		}
		if(swapped==0)
			break;
	}
	
}
//==============================================
//Load data from a file and add it to the Linked List
void MyLinkedList::loadData(string path)
{
	ifstream myFile;
	myFile.open(path);
	head=NULL;
	Node* tail=NULL;
	if(!myFile){
		cout<<"No Such File"<<endl;
	}
	else if(myFile.is_open()){
		string line;
		while (getline(myFile, line)){
			stringstream s(line);
			int elem=0;
			s>>elem;
			Node* newnode = new Node(elem); 
			if(head == NULL){
				head = newnode;
				tail = newnode;
			}

			else{
				tail->next = newnode;
				tail = tail->next;
			}

		}
	myFile.close();
	}
	//todo

}
//=============================================
//Dump/write the contents of the list to a file
void MyLinkedList::dumpData(string path) const
{
	ofstream myfile;
	myfile.open(path);
	Node* current=head;
	if(myfile.is_open()){
		while (current!= NULL){
			myfile<<current->elem<<endl;
			current=current->next;
		}
		myfile.close();
	}

	//todo
}
//==================================================

