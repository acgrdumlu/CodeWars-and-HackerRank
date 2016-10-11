class User():
    def __init__(self, rank=0, progress=0):
        self.rank = rank
        self.progress = progress

    def inc_progress(self, task_rank):
        # Raises an error for invalid task ranks
        if task_rank > 8 or task_rank < -8 or task_rank == 0:
            raise ValueError('Task Rank invalid')

        # Initialize user if never done so before
        if self.rank == 0:
            self.rank = -8

        # Calculate rank difference while accounting for missing 0 rank
        # Negative rank_diff = easier task
        # Positive rank_diff = harder task
        rank_diff = task_rank - self.rank
        if task_rank > self.rank:
            if task_rank > 0 and self.rank < 0:
                rank_diff -= 1
        elif task_rank < self.rank:
            if task_rank < 0 and self.rank > 0:
                rank_diff += 1

        # Easier task by 1 rank, anything easier than that receives 0 progress
        if rank_diff == -1:
            self.progress += 1
        # Equal task
        elif rank_diff == 0:
            if self.rank != 8:
                self.progress += 3
        # Harder task
        elif rank_diff > 0:
            self.progress += 10 * rank_diff * rank_diff

        # Applies progression to rank and progress meter
        if self.progress >= 100:
            # Handles missing 0 rank scenario
            initial_rank = self.rank
            levels = (int)(self.progress / 100)
            if initial_rank < 0 and initial_rank + levels >= 0:
                self.rank += levels + 1
            else:
                self.rank += levels

            # Handles max rank scenario
            if self.rank >= 8:
                self.rank = 8
                self.progress = 0
            else:
                self.progress -= levels * 100