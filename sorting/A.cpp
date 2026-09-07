#include <iostream>
#include <vector>
#include <string>
#include <sstream>
using namespace std;

void SelectionSort(vector<int>& arr){
    int n = arr.size();
    for (int i = 0; i < n-1; i++){
        int minIndex = i;
        for (int j = i+1; j < n; j++){
            if (arr[j] > arr[minIndex]){
                minIndex = j;
            }
        }
        swap(arr[i], arr[minIndex]);
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
    SelectionSort(arr);

    for (int i = 0; i < arr.size(); i++){
        cout << arr[i] << " ";
    }
    return 0;
}