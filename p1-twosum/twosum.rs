impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut ind1: u32 = 0;
        let mut ind2: u32 = 1;
        let numLength = nums.len() as u32;
        let mut result = vec![0,0];
        while ind1 < numLength {
            ind2 = ind1 + 1;
            while ind2 < numLength {
                if nums[ind1 as usize] + nums[ind2 as usize] == target {
                    result[0] = ind1 as i32;
                    result[1] = ind2 as i32; 
                    return result;
                } else {
                    ind2 = ind2 + 1;
                }
            }
            ind1 = ind1 + 1;
        }
        return result;
    }
}
