class RequestVote:
    def __init__(self, term, candidate_id):
        self.term = term
        self.candidate_id = candidate_id


class AppendEntries:
    def __init__(self, term, leader_id, entries=None):
        self.term = term
        self.leader_id = leader_id
        self.entries = entries or []
