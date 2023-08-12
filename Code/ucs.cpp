#include <iostream>
#include <vector>
#include <limits.h>
#include <map>
#include <queue>
using namespace std;

const int N = 1e5 + 10;
vector<vector<int>> g(N);
map<pair<int, int>, int> cost;

int ucs(int start, int goal)
{
    int ans = INT_MAX;
    priority_queue<pair<int, int>> q;
    q.push(make_pair(0, start));

    map<int, int> visited;

    while (q.size() > 0)
    {
        pair<int, int> p = q.top();
        q.pop();
        p.first *= -1;

        if (p.second == goal)
        {
            ans = p.first;

            q.pop();
            return ans;
        }

        if (visited[p.second] == 0)
            for (int i = 0; i < g[p.second].size(); i++)
            {
                q.push(make_pair((p.first + cost[make_pair(p.second, g[p.second][i])]) * -1, g[p.second][i]));
            }

        visited[p.second] = 1;
    }

    return ans;
}

int main()
{
    int n;
    cin >> n;

    for (int i = 0; i < n - 1; i++)
    {
        int x, y, z;
        cin >> x >> y >> z;
        g[x].push_back(y);
        g[y].push_back(x);
        cost[make_pair(x, y)] = z;
    }

    int start, goal;
    cin >> start >> goal;

    cout << "Cost from node " << start << " to node " << goal << ": " << ucs(start, goal) << endl;
    ;
}