from config.config import WINDOW_HEIGHT, WINDOW_WIDTH, WIDTH_OFFSET, HEIGHT_OFFSET

class Window:
    def __init__(self):
        """
        Creates a 2D array of size height x width
        with a border of size height_offset and width_offset
        """
        self.height = WINDOW_HEIGHT
        self.width = WINDOW_WIDTH
        
        self.height_offset = HEIGHT_OFFSET
        self.width_offset = WIDTH_OFFSET

        self.available_height_range = (self.height_offset, self.height - self.height_offset)
        self.available_width_range = (self.width_offset, self.width - self.width_offset)

        self.available_width_value = self.available_width_range[1] - self.available_width_range[0]
        self.available_height_value = self.available_height_range[1] - self.available_height_range[0]

        self.__build_array()

    def __build_array(self):
        """
        Builds the 2D array and sets the boundary
        """
        self.array = [[" " for j in range(self.width)] for i in range(self.height)]
        self.__set_boundary()

    def __set_boundary(self):
        """
        Sets the boundary of the 2D array"""
        self.left_boundary = [(0,y) for y in range(0, self.height)]
        self.right_boundary = [(self.width - 1, y) for y in range(0, self.height)]
        self.bottom_boundary = [(x, self.height - 1) for x in range(0, self.width)]
        self.top_boundary = [(x, 0) for x in range(0, self.width)]

        self.offset_left_boundary = [(int(self.width_offset / 2), y) for y in range(int(self.height_offset / 2), int(self.available_height_range[1] + self.height_offset / 2))]
        self.offset_right_boundary = [(int(self.width - self.width_offset / 2 - 1), y) for y in range(int(self.height_offset / 2), int(self.available_height_range[1] + self.height_offset / 2))]
        self.offset_bottom_boundary = [(x, int(self.height - self.height_offset / 2 - 1)) for x in range(int(self.width_offset / 2), int(self.available_width_range[1] + self.width_offset / 2))]
        self.offset_top_boundary = [(x, int(self.height_offset / 2)) for x in range(int(self.width_offset / 2), int(self.available_width_range[1] + self.width_offset / 2))]

        corners = [(0, 0), (0, self.height - 1), (self.width - 1, 0), (self.width - 1, self.height - 1), (int(self.width_offset / 2), int(self.height_offset / 2)), (int(self.width_offset / 2), int(self.height - self.height_offset /2 - 1)), (int(self.width - self.width_offset / 2 - 1), int(self.height_offset / 2)), (int(self.width - self.width_offset / 2 - 1), int(self.height - self.height_offset / 2 - 1))]

        boundaries = [self.left_boundary, self.right_boundary, self.bottom_boundary, self.top_boundary, self.offset_left_boundary, self.offset_right_boundary, self.offset_bottom_boundary, self.offset_top_boundary]
        signs = ['|','|','-','-','|','|','-','-']
        for boundary, sign in zip(boundaries, signs):
            for element in boundary:
                self.set_array_value(element[0], element[1], sign)
        for corner in corners:
            self.set_array_value(corner[0], corner[1], '+')

        
                

    def set_array_value(self, x_pos: int, y_pos: int, value: str):
        """
        Sets the value at the given position in the 2D array to the given value
        """
        self.array[y_pos][x_pos] = value

    def get_array_value(self, x_pos: int, y_pos: int) -> str:
        """
        Gets the value at the given position in the 2D array
        """
        return self.array[x_pos][y_pos]

    def render_array(self) -> str:
        result_string = ""
        for i in range(0, self.height):
            row = ""
            for j in range(0, self.width):
                row += self.array[i][j]
            result_string += row + "\n"
        return result_string
    


def create_plot(x_time_data: list[str], y_data: list[float], latitude: float, longitude: float, city: str = None) -> str:
    """
    Creates a plot of the given x and y data
    """
    if len(x_time_data) != len(y_data):
        raise Exception("X_DATA AND Y_DATA HAVE TO BE OF THE SAME LENGTH")
    y_min = min(y_data)
    y_max = max(y_data)

    x_data = list(range(len(x_time_data)))
    x_min = min(x_data)
    x_max = max(x_data)

    new_plot = Window()

    y_axis_labels = [y_min, (y_min + y_max) / 2, y_max]
    x_axis_labels = [x_time_data[0], x_time_data[len(x_time_data) // 2], x_time_data[-1]]

    for i, label in enumerate(y_axis_labels):
        normalized_y = 1 - (label - y_min) / (y_max - y_min)
        y_location = int(round(normalized_y * new_plot.available_height_value + new_plot.height_offset, 0))
        label_str = f"{label:.2f}"
        for j, char in enumerate(label_str, start=new_plot.width_offset - len(label_str)- new_plot.width_offset//7):
            new_plot.set_array_value(j, y_location, char)

    for i, label in enumerate(x_axis_labels):
        if i == 0:
            x_location = new_plot.width_offset
        elif i == 1:
            x_location = int(round(new_plot.available_width_value / 2 + new_plot.width_offset / 2, 0))
        else:
            x_location = new_plot.width - new_plot.width_offset - len(label)
        
        for j, char in enumerate(label):
            new_plot.set_array_value(x_location + j, new_plot.height - new_plot.height_offset + 1, char)
    if city:
        title = f"7 Day Forecast for {city} (Lat: {latitude}, Lon: {longitude})"
    else:   
        title = f"7 Day Forecast for Latitude: {latitude}, Longitude: {longitude}"
    title_start = (new_plot.width - len(title)) // 2
    for i, char in enumerate(title):
        new_plot.set_array_value(title_start + i, 1, char)

    for x, y in zip(x_data, y_data):
        #COORDINATE SYSTEM STARTS AT LEFT TOP CORNER
        #X AXIS -> X
        #Y AXIS -> -Y
        normalized_x = (x - x_min) / (x_max - x_min)
        normalized_y = 1 - (y - y_min) / (y_max - y_min)

        x_location = int(round(normalized_x * new_plot.available_width_value + new_plot.width_offset,0))
        y_location = int(round(normalized_y * new_plot.available_height_value + new_plot.height_offset, 0))

        new_plot.set_array_value(x_location, y_location, '+')

    
    return new_plot.render_array()