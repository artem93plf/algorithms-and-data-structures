#include <iostream>
#include <vector>
#include <string>
#include <sstream>
using namespace std;

void BubbleSort(vector<int>& arr){
    int n = arr.size();
    for (int i = 0; i < n - 1; i++){
        bool swapped = false;
        for (int j = 0; j < n - 1 - i; j++){
            if (arr[j] < arr[j+1]) {
                swap(arr[j], arr[j+1]);
                swapped = true;
            }
        }
        if (!swapped){
            break;
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

    BubbleSort(arr);

    for (int i = 0; i < arr.size(); i++){
        cout << arr[i] << " ";
    }
    return 0;
}