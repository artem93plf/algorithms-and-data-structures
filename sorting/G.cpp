#include <iostream>
#include <vector>
#include <algorithm>
#include <sstream>
using namespace std;

void CountingSort(vector<int>& arr) {
    int n = arr.size();
    int maxElement = *max_element(arr.begin(), arr.end());
    vector<int> count(maxElement + 1, 0);
    vector<int> output;

    for (int i = 0; i < n; i++) {
        count[arr[i]]++;
    }
    
    for (int num = 0; num <= maxElement; num++) {
        for (int j = 0; j < count[num]; j++) {
            output.push_back(num);
        }
    }
    arr = output;
}

int main() {
    vector<int> arr;
    string line;
    getline(cin, line);
    stringstream ss(line);
    int x;
    while (ss >> x) {
        arr.push_back(x);
    }
    CountingSort(arr);
    

    for (int num : arr) {
        cout << num << " ";
    }

    return 0;
}