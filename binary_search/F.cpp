#include <iostream>
#include <vector>

using namespace std;

bool good(int cnt, int q, int s, int t){
    return t / q + t / s >= cnt;
}

int main() {
    int n, q, s;
    cin >> n >> q >> s;

    if (q > s) {
        swap(q, s);
    }

    int l = 0;
    int r = (n - 1) * s;

    while (r - l > 1) {
        int mid = (l + r) / 2;
        if (!good(n - 1, q, s, mid)) {
            l = mid;
        } else {
            r = mid;
        }
    }

    cout << r + q;
    return 0;
}
