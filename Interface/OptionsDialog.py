import arcade
from typing import List
class OptionsDialog:
    def __init__(self,options:List[str],pos_x,pos_y,width,height,margin:int):
        self.options = options
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height
        self.margin = margin

        #4 vertices of the rectangle, order matters
        #complex but faster to draw
        self.point_list = []
        self.color_list = []

        
        for i, option in enumerate(self.options):
            #Set the position of the option
            subheight = int(round(height/len(self.options),0))
            subposition_y =  int(round(self.pos_y + i*self.margin + i*subheight,0))           

            top_left = (self.pos_x,subposition_y)
            top_right = (self.pos_x+width,subposition_y)
            bottom_left = (self.pos_x,subposition_y+subheight)
            bottom_right = (self.pos_x+width,subposition_y+subheight)

            self.point_list.append(top_left)
            self.point_list.append(top_right)
            self.point_list.append(bottom_right)
            self.point_list.append(bottom_left)
            for j in range(4):
                self.color_list.append((0,50,0+i*50))          

        print("end")
    def __repr__(self) -> str:
        return f"OptionDialog(options={self.options},pos_x={self.pos_x},pos_y={self.pos_y},width={self.width},height={self.height},margin={self.margin})"

    def get_points(self)->List[int]:
        return self.point_list

    def get_colors(self):
        return self.color_list
    


