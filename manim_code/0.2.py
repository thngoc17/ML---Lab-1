from manim import *
import numpy as np

class DiffusionNoise(Scene):
    def construct(self):
        # 1. Tạo một mảng nhiễu Gaussian ban đầu (sử dụng ImageMobject để render nhanh)
        def get_noise_image():
            # Tạo mảng ngẫu nhiên 128x128 để giả lập nhiễu hạt mè
            noise_array = np.random.randint(0, 256, (128, 128, 3), dtype=np.uint8)
            return ImageMobject(noise_array).scale(4) # Phóng to để thấy rõ hạt

        noise_img = get_noise_image()
        
        # 2. Tiêu đề xuất hiện (Phù hợp với Audio: "Diffusion Models")
        title = Text("DIFFUSION MODEL", font_size=42, color=BLUE_A)
        title.add_background_rectangle(opacity=0.8, color=BLACK)
        title.to_edge(UP)

        # 3. Hiệu ứng nhiễu động (Dynamic Noise)
        # Chúng ta sẽ cập nhật liên tục hình ảnh nhiễu để tạo cảm giác "sôi động"
        noise_group = Group(noise_img)
        
        def update_noise(mob):
            new_noise = get_noise_image()
            mob.replace(new_noise)

        # 4. Bắt đầu phân cảnh
        self.play(FadeIn(noise_img), run_time=1)
        self.wait(0.5)

        # Bắt đầu hiệu ứng nhiễu nhảy múa
        noise_img.add_updater(update_noise)
        
        # Hiển thị văn bản AI
        self.play(Write(title), run_time=1.5)
        
        # Tạo một khung quét (Scanning line) để thể hiện AI đang "nhìn" vào nhiễu
        scan_line = Line(LEFT*4, RIGHT*4, color=BLUE_A).set_stroke(width=10)
        scan_line.set_glow_factor(1)
        scan_line.move_to(noise_img.get_top())

        # 5. Diễn biến chính (8-10 giây)
        # Quét từ trên xuống dưới để mô phỏng quá trình xử lý
        self.play(
            scan_line.animate.move_to(noise_img.get_bottom()),
            run_time=3,
            rate_func=linear
        )
        self.play(
            scan_line.animate.move_to(noise_img.get_top()),
            run_time=2,
            rate_func=linear
        )

        # Thông báo trạng thái
        status_text = Text("Analyzing Chaos...", font_size=24, color=WHITE).next_to(noise_img, DOWN)
        self.play(FadeIn(status_text))
        
        self.wait(2) # Giữ khung hình cho đủ 10s tổng cộng

        # Kết thúc: Làm mờ dần để chuyển cảnh cho Editor C
        noise_img.remove_updater(update_noise)
        self.play(
            FadeOut(noise_img),
            FadeOut(title),
            FadeOut(status_text),
            FadeOut(scan_line),
            run_time=1
        )

# Ghi chú cho Người B:
# - Để chạy code này: manim -pql file_name.py DiffusionNoise
# - Độ phân giải thấp (l) giúp render nhanh để kiểm tra. 
# - Khi render bản cuối nên dùng -pqh để có chất lượng HD.