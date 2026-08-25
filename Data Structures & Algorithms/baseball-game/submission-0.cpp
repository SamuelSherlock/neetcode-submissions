class Solution {
public:
    int calPoints(vector<string>& operations) {
        std::vector<int> record;
        int sum = 0;
        for(int i = 0; i < operations.size(); i++) {
            if (operations[i] == "+") {
                int num = record[record.size()-2] + record.back();
                record.push_back(num);
                sum += num;
            } else if (operations[i] == "C") {
                sum -= record.back();
                record.pop_back();
            } else if (operations[i] == "D") {
                int num = record.back() *2;
                record.push_back(num);
                sum += num;
            } else {
                int num = std::stoi(operations[i]);
                record.push_back(num);
                sum+= num;
            }
        }
        return sum;
    }
};