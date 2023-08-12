// BIJON SAHA DURJOY
//    SUST_SWE_19
#include <bits/stdc++.h>
#define ll long long
using namespace std;

const int N = 1e5 + 2;
vector<int> v[N];
bool visited[N];

void dfs(int source)
{
    cout<<source<<" ";
    visited[source] = true;
    for(int child : v[source])
    {
        if(!visited[child])
        {
            dfs(child);
        }
    }

}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin>>n;
    int x,y;
    for(int i =0; i<n-1; i++)
    {
        cin>>x>>y;
        v[x].push_back(y);
        v[y].push_back(x);
    }
    dfs(1);
    return 0;
}