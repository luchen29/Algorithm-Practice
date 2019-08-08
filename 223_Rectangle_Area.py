class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        firstArea, secondArea = (C - A) * (D - B), (G - E) * (H - F)
        if self.hasSharedArea(A,B,C,D,E,F,G,H):
            if A<=E and B<=F and C>=G and D>=H:
                return firstArea
            elif E<A and F<B and G>C and H>D:
                return secondArea
            else:
                sharedWidth = min(C-E, G-A, G-E, C-A)
                sharedArea = min(H-B, D-F, H-F, D-B)
                return firstArea + secondArea - sharedWidth*sharedArea
        else: 
            return firstArea + secondArea
    
    def hasSharedArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int):
        if B>=H or D<=F or C<=E or A>=G:
            return False
        return True
    