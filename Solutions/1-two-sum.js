var twoSum = function(nums, target) {
    // maps the index

    const seen = new Map();
    
    for (let i = 0; i < nums.length; i++) {
        // value needed to pair with target

        const need = target - nums[i];
        
        if (seen.has(need)) {
            return [seen.get(need), i];
        }
        
        // if seen its done, if not its remembered for later

        seen.set(nums[i], i);
    }

    // guarantees 1 answer

    return[];
};