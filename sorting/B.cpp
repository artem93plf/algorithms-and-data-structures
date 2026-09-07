#include <iostream>
#include <vector>
#include <string>
#include <sstream>
using namespace std;

void InsertionSort(vector<int>& arr){
    int n = arr.size();
    for (int i = 1; i < n; i++){
        int key = arr[i];
        for (int j = i-1; j>=0; j--){
            if (arr[j] < key){
                break;
            }
            arr[j+1] = arr[j];
            arr[j] = key;
        }
    }
}

int main(){
    vector<int> arr;
    int x;
    string line;
    getline(cin, line);
    stringstream nums(line);
    while (nums >> x){
        arr.push_back(x);
    }
    InsertionSort(arr);
    for (int i = 0; i < arr.size(); i++){
        cout << arr[i] << " ";
    }
    return 0;
}