class CircularList(list):
    """List but you can have index and slices out of range"""
    def __getitem__(self, key):
        if isinstance(key, slice ) :
            # Get the start, stop, and step from the slice without ceiling the stop
            start, stop, step = key.indices(10**6)
            if stop < start and step > 0: # From left to right
                return [self[i] for i in range(start,stop+len(self),step)]
            elif stop > start and step < 0: # From right to left
                return [self[i] for i in range(start+len(self),stop,step)]
            else:
                return [self[i] for i in range(start,stop,step)]
        elif isinstance( key, int ) :
            return super(CircularList, self).__getitem__(key % len(self))
        else:
            raise TypeError("Invalid argument type.")
