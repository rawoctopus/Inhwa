/*
2019.07.27
Inhwa Kwak
https://programmers.co.kr/learn/courses/30/lessons/42889
*/

#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool compare(pair<double,int> a, pair<double,int> b){
    if(a.first == b.first)
        return a.second < b.second;

    return a.first > b.first;
}

vector<int> solution(int N, vector<int> stages) {
    vector<int> answer;
    vector<pair<float,int>> fail_stage;
    int num_players = stages.size();
    int players[511] = {0,};
    
    for(vector<int>::iterator iter = stages.begin(); iter!=stages.end(); iter++)
        players[*iter-1]++;

    for(int i=1; i<=N; i++){
        if(players[i-1] == 0)
            fail_stage.push_back(make_pair(0,i));
        else{
            fail_stage.push_back(make_pair((float)players[i-1]/num_players, i));
            num_players -= players[i-1];
        }
    }

    sort(fail_stage.begin(), fail_stage.end(), compare);

    for(vector<pair<float,int>>::iterator iter = fail_stage.begin(); iter!=fail_stage.end(); iter++)
        answer.push_back(iter->second);

    return answer;
}