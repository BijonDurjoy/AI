// BIJON SAHA DURJOY
//    SUST_SWE_19
#include <bits/stdc++.h>
#define ll long long
using namespace std;

const int N = 1e5 + 2;
vector<int> v[N];
bool visited[N];

void bfs(int source)
{
    queue<int>q;
    q.push(source);
    visited[source] = true;

    while(!q.empty())
    {
        int cur_v = q.front();
        q.pop();
        cout<<cur_v<<" ";

        for(int child : v[cur_v])
        {
            if(!visited[child])
            {
                q.push(child);
                visited[child] = true;
            }
        }
    }
    
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin>>n;
    
    for(int i=0; i<n-1; i++)
    {
        int x,y;
        cin>>x>>y;
        v[x].push_back(y);
        v[y].push_back(x);
    }
    return 0;
}