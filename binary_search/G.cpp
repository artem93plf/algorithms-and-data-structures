#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool good(vector<int>& ropes, int k, int r) {
    long long cnt = 0;
    for (int length : ropes) {
        cnt += length / r;
    }
    return cnt >= k;
}

int main() {
    int n, k;
    cin >> n >> k;

    vector<int> ropes(n);
    for (int i = 0; i < n; i++) {
        cin >> ropes[i];
    }
    long long s = 0;
    for (int length : ropes) {
        s += length;
    }
    if (s < k) {
        cout << 0;
        return 0;
    }

    int l = 0;
    int r = *max_element(ropes.begin(), ropes.end()) + 1;

    while (r - l > 1) {
        int mid = (l + r) / 2;
        if (good(ropes, k, mid)) {
            l = mid;
        } else {
            r = mid;
        }
    }
   cout << l;
   return 0;
}

     
