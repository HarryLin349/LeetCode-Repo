using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int curStreak = 0;
        int curMax = 0;
        int lastReset = 0;
        unordered_map <char, int> seenChars;
        for (int i = 0; i < s.length(); i++){
            auto search = seenChars.find(s[i]);
            if (search == seenChars.end()){
                // cur char hasnt been seen
                seenChars.insert(make_pair(s[i], i));
                curStreak++;
                // cout << "adding " << s[i] <<" at " << i << " for streak " << curStreak << endl;
            } else {
                if (search->second < lastReset){
                    // cur char seen before a reset
                    // cout << "found dup" << search->first << "at " << search->second << "before reset" << lastReset << endl;
                    search->second = i;
                    curStreak++;
                } else {
                    // cur char seen after a reset
                    curStreak = i - search->second;
                    // curStreak -= search->second;
                    // lastReset += 1;
                    lastReset = search->second;
                    // cout << "duplicate "<< s[i] << " at " << i << " last occ " << search->second << " old->new streak " << curStreak + search->second << "->" << curStreak << endl;            
                    search->second = i;
                    // cout << "reset to " << i << endl;                    
                }

            }
            if (curStreak > curMax){
                // cout << "  ==new max " << curStreak << endl;
                curMax = curStreak;
            }
        }
        return curMax;
    }
};
