class SegmentTree:
    def __init__(self, data, merge):
        # data:传入的数组
        # merge:处理的业务逻辑，例如求和/最大值/最小值，lambda表达式
        self.data = data
        self.n = len(data)
        self.tree = [None] * 4 * self.n
        self._merge = merge
        if self.n:
            self._build(0, 0, self.n - 1)

    def _build(self,idx,l,r):
        if l==r:
            self.tree[idx]=self.data[l]
            return
        mid=(l+r)//2
        left,right=2*idx+1,2*idx+2
        self._build(left,l,mid)
        self._build(right,mid+1,r)
        self.tree

