class Solution:
    def trap(self, height: List[int]) -> int:
        starting_idxs = []
        # start from left, keeping track of slope
        # if the adjacent block is smaller than the current,
        # then mark slope = down
        # keep track until adjacent block is larger than current
        # the interval between the last drop down and the rise up is the trough of a well which can trap rain water
        # find all such wells

        # we have two options: we can get the well indices first, then compute total trapped water size
        # or we could try and compute on the fly
        # to compute on the fly, we can track height * length of the area we've covered so far from left to right. the important part is that if the right side is low, we need to make sure not to count cells above that height
        # could do that by storing left_brim_height, as we go from left to right we accumulate left_brim_height - bar_height in a list. then once we've found the right_brim_height, we can sum over the accumlated values, taking the max(right_brim_height, value_i)
