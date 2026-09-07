#include <iostream>
#include <vector>
using namespace std;

int BubbleSort(vector<int>& arr){
    int n = arr.size();
    int count = 0;
    for (int i = 0; i < n - 1; i++){
        bool swapped = false;
        for (int j = 0; j< n-1-i;j++){
            if (arr[j] > arr[j+1]) {
                swap(arr[j], arr[j+1]);
                swapped = true;
                count++;
            }
        }
        if (!swapped) {
            break;
        }
    }
    return count;
}

int main(){
    int n;
    cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++){
        cin >> arr[i];
}
    int swaps = BubbleSort(arr);
    cout << swaps << endl;
    return 0;
}