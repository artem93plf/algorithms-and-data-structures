#include <iostream>
#include <vector>

using namespace std;

bool good(vector<int> boxes, int k, int r) {
    int cows_count = 1;
    int last_box = boxes[0];
    for (int i = 1; i < boxes.size(); i++) {
        if ((boxes[i] - last_box) >= r) {
            cows_count++;
            last_box = boxes[i];
        }
    }
    return cows_count >= k;
}

int main() {
    int n, k;
    cin >> n >> k;
    
    vector<int> boxes(n);
    for (int i = 0; i < n; i++) {
        cin >> boxes[i];
    }

    int l = 0;
    int r = boxes[n - 1] - boxes[0] + 1;
    
    while (r - l > 1) {
        int mid = (l + r) / 2;
        if (good(boxes, k, mid)) {
            l = mid;
        } else {
            r = mid;
        }
    }

    cout << l;
    return 0;
}