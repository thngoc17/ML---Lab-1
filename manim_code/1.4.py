from manim import *
import numpy as np

class Scene4MoLRG(ThreeDScene):
    def construct(self):
        # Thiết lập màu sắc chuẩn 3b1b style
        DOT_COLOR = YELLOW_D
        SURFACE_COLOR = BLUE_E
        TEXT_COLOR = WHITE
        
        # ---------------------------------------------------------
        # [3:35 - 3:55] SỰ KIỆN 1: Curse of Dimensionality
        # ---------------------------------------------------------
        
        # 1. Tạo không gian 3D
        axes = ThreeDAxes(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            z_range=[-4, 4, 1],
            axis_config={"color": GREY_B, "stroke_width": 2}
        )
        
        # 2. Định nghĩa mặt phẳng không gian con ẩn (Intrinsic Manifold)
        # Bằng cách kết hợp tuyến tính 2 vector cơ sở
        v1 = np.array([1, 1.5, 0.5])
        v2 = np.array([-1.5, 1, 1])
        # Chuẩn hóa các vector cơ sở
        v1 = v1 / np.linalg.norm(v1)
        v2 = v2 / np.linalg.norm(v2)

        # 3. Rải các điểm dữ liệu lơ lửng
        # Các điểm này THỰC CHẤT nằm trên mặt phẳng sinh bởi v1, v2
        dots = VGroup()
        np.random.seed(42) # Giữ nguyên seed để animation đồng nhất
        for _ in range(50):
            c1 = np.random.uniform(-3, 3)
            c2 = np.random.uniform(-3, 3)
            # Thêm một chút xíu nhiễu rất nhỏ để trông tự nhiên hơn nếu cần, 
            # nhưng ở đây ta ép chúng nằm hoàn toàn trên mặt phẳng để tạo sự bất ngờ
            point = c1 * v1 + c2 * v2
            dot = Dot3D(point=point, color=DOT_COLOR, radius=0.08)
            dots.add(dot)

        # Đặt camera ở góc nhìn khiến các điểm trông như một đám mây 3D lộn xộn
        self.set_camera_orientation(phi=65 * DEGREES, theta=30 * DEGREES)
        
        # Hiện chữ "Curse of Dimensionality" (cố định trên màn hình 2D)
        title_curse = Text("Curse of Dimensionality", font_size=40, color=WHITE).to_corner(UL)
        self.add_fixed_in_frame_mobjects(title_curse)

        self.play(Create(axes), run_time=2)
        self.play(FadeIn(dots), run_time=2)
        
        # Xoay camera từ từ để thấy sự trống trải của không gian d-chiều
        self.begin_ambient_camera_rotation(rate=0.1)
        self.wait(16) # Khớp với thời lượng 20 giây đầu tiên (đã trừ thời gian play)
        self.stop_ambient_camera_rotation()

        # ---------------------------------------------------------
        # [3:55 - 4:20] SỰ KIỆN 2: Intrinsic Dimension
        # ---------------------------------------------------------
        
        title_blessing = MathTex(r"\text{Intrinsic Dimension } r \ll d", font_size=42, color=TEAL_C).to_corner(UL)
        self.add_fixed_in_frame_mobjects(title_blessing)
        
        # Đổi chữ mượt mà
        self.play(Transform(title_curse, title_blessing), run_time=1.5)

        # Tạo mặt phẳng 2D đi qua các điểm
        plane = Surface(
            lambda u, v: u * v1 + v * v2,
            u_range=[-3.5, 3.5],
            v_range=[-3.5, 3.5],
            resolution=(15, 15),
            fill_opacity=0.3,
            fill_color=SURFACE_COLOR,
            stroke_width=0.5,
            stroke_color=BLUE_C
        )

        # ANIMATION CHÍNH: Camera di chuyển về góc nhìn "cắt ngang" mặt phẳng
        # Tính toán góc phi, theta sao cho góc nhìn song song với mặt phẳng
        # Vector pháp tuyến của mặt phẳng:
        normal = np.cross(v1, v2)
        normal = normal / np.linalg.norm(normal)
        
        # Sử dụng góc nhìn hé lộ (nhìn dọc theo mép mặt phẳng rồi hơi nâng lên)
        self.move_camera(phi=80 * DEGREES, theta=-45 * DEGREES, run_time=4, rate_func=there_and_back_with_pause)
        
        self.play(FadeIn(plane), run_time=2)
        
        # Xoay camera đến góc nhìn đẹp nhất để ngắm mặt phẳng
        self.move_camera(phi=60 * DEGREES, theta=60 * DEGREES, run_time=3)
        self.wait(14.5) # Chờ phần voiceover giải thích sự tồn tại của mặt phẳng

        # ---------------------------------------------------------
        # [4:20 - 4:45] SỰ KIỆN 3: Công thức MoLRG & Basis Vectors
        # ---------------------------------------------------------
        
        # Hiện công thức toán học
        formula = MathTex(
            r"p_{data}(x) = \frac{1}{K} \sum_{i=1}^K \mathcal{N}(x; 0,", 
            r"U_i U_i^T", 
            r")",
            font_size=40
        ).to_corner(UR)
        # Đổi màu phần ma trận hiệp phương sai hạng thấp để nhấn mạnh
        formula[1].set_color(YELLOW_C)
        
        self.add_fixed_in_frame_mobjects(formula)
        self.play(Write(formula), run_time=2)

        # Vẽ hệ vector cơ sở U_i ngay trên mặt phẳng
        vec_u1 = Arrow3D(start=ORIGIN, end=v1 * 2, color=ORANGE, thickness=0.02)
        vec_u2 = Arrow3D(start=ORIGIN, end=v2 * 2, color=GREEN_C, thickness=0.02)

        # Nhãn cho vector (để hiển thị trong không gian 3D, Text/MathTex thường bị lỗi khi xoay, 
        # nên ta gắn fixed in frame thông qua update function hoặc chỉ cần dùng màu sắc)
        # Ở đây ta dùng cách đổi màu trong công thức để người xem tự liên hệ.
        
        self.play(FadeIn(vec_u1, scale=0.5), FadeIn(vec_u2, scale=0.5), run_time=2)
        
        # Xoay nhẹ nhàng để chiêm ngưỡng toàn bộ cấu trúc kết thúc scene
        self.begin_ambient_camera_rotation(rate=0.08)
        self.wait(21) # Chờ nốt phần voiceover