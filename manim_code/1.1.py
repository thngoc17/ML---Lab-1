from manim import *
import numpy as np

class ReproducibilityScene(MovingCameraScene):
    def construct(self):
        # Thiết lập màu sắc nền mang phong cách 3b1b (tùy chọn, ở đây ta dùng nền đen mặc định)
        self.camera.background_color = BLACK

        # =====================================================================
        # SCENE 1: LỜI NGỎ VÀ HIỆN TƯỢNG TÁI TẠO
        # =====================================================================

        # ---------------------------------------------------------------------
        # [0:00 - 0:15]: Khởi tạo nhiễu Gaussian x_T và tách thành 3 bản
        # ---------------------------------------------------------------------
        
        # Tạo mảng nhiễu Gaussian bằng numpy (tránh dùng shader phức tạp, đảm bảo tính chân thực của pixel)
        np.random.seed(42)
        noise_arr = np.random.randint(0, 256, (100, 100, 3)).astype('uint8')
        base_noise_img = ImageMobject(noise_arr)
        base_noise_img.height = 4 # Phóng to để người xem thấy rõ hạt nhiễu
        
        # Nhãn toán học đặc trưng
        noise_label = MathTex("x_T").scale(1.5).next_to(base_noise_img, UP)

        # 0:00 - 0:05: Hiện nhiễu và nhãn
        self.play(
            FadeIn(base_noise_img, shift=UP*0.5),
            Write(noise_label),
            run_time=3
        )
        self.wait(2)

        # Tạo 3 bản sao
        noise_1 = base_noise_img.copy()
        noise_2 = base_noise_img.copy()
        noise_3 = base_noise_img.copy()

        # Vị trí mục tiêu cho 3 góc (Tạo thành một tam giác cân đối trên màn hình)
        pos_1 = UP * 1.5 + LEFT * 4
        pos_2 = UP * 1.5 + RIGHT * 4
        pos_3 = DOWN * 2

        # 0:05 - 0:15: Phân tách nhiễu thành 3 bản sao trượt về 3 góc
        self.play(FadeOut(noise_label), run_time=1)
        self.play(
            LaggedStart(
                base_noise_img.animate.scale(0.6).move_to(pos_1),
                FadeIn(noise_2.scale(0.6).move_to(pos_2), shift=RIGHT),
                FadeIn(noise_3.scale(0.6).move_to(pos_3), shift=DOWN),
                lag_ratio=0.3
            ),
            run_time=5,
            rate_func=smooth
        )
        # Gán lại tên biến cho dễ thao tác, biến base_noise_img giờ là noise_1
        noise_1 = base_noise_img 
        self.wait(4)

        # ---------------------------------------------------------------------
        # [0:15 - 0:35]: Các kiến trúc mạng (U-Net, DiT, EDM) và quá trình Giải nhiễu
        # ---------------------------------------------------------------------
        
        # Khung viền (thay vì viền trơn, ta dùng màu gradient để tạo sự sang trọng)
        box_1 = SurroundingRectangle(noise_1, color=TEAL, buff=0.1).set_stroke(width=3)
        box_2 = SurroundingRectangle(noise_2, color=MAROON, buff=0.1).set_stroke(width=3)
        box_3 = SurroundingRectangle(noise_3, color=GOLD, buff=0.1).set_stroke(width=3)

        # Tên kiến trúc chuyển sang chuẩn LaTeX (Computer Modern font)
        # Sử dụng Tex() thay vì Text(), scale chỉnh lên 0.8 một chút để dễ đọc hơn
        label_1 = Tex("U-Net").scale(0.8).next_to(box_1, UP)
        label_2 = Tex("DiT").scale(0.8).next_to(box_2, UP)
        
        # Nhãn EDM đã được chuyển lên trên (UP) để nhường không gian phía dưới cho phụ đề
        label_3 = Tex("EDM").scale(0.8).next_to(box_3, UP) 

        # 0:15 - 0:22: Vẽ khung và hiện tên kiến trúc
        self.play(
            AnimationGroup(
                Create(box_1), Write(label_1),
                Create(box_2), Write(label_2),
                Create(box_3), Write(label_3),
                lag_ratio=0.2
            ),
            run_time=4
        )
        self.wait(3)

        # Quá trình giải nhiễu (Denoising)
        # *LƯU Ý*: Cần có file "face_target.jpg" trong thư mục chứa code
        # Để code chạy được ngay cả khi chưa có ảnh, mình sẽ bọc trong try-except 
        # và dùng một mảng màu gradient làm ảnh giả lập nếu thiếu file.
        try:
            face_1 = ImageMobject("raw_media/cat.jpeg").match_height(noise_1).move_to(pos_1)
            face_2 = ImageMobject("raw_media/cat.jpeg").match_height(noise_2).move_to(pos_2)
            face_3 = ImageMobject("raw_media/cat.jpeg").match_height(noise_3).move_to(pos_3)
        except:
            # Ảnh giả lập (Mô phỏng một bức ảnh đã được giải nhiễu mượt mà)
            clean_arr = np.zeros((100, 100, 3), dtype=np.uint8)
            clean_arr[:, :, 0] = np.linspace(0, 255, 100).reshape(1, 100) # Red gradient
            clean_arr[:, :, 1] = np.linspace(255, 0, 100).reshape(100, 1) # Green gradient
            face_1 = ImageMobject(clean_arr).match_height(noise_1).move_to(pos_1)
            face_2 = ImageMobject(clean_arr).match_height(noise_2).move_to(pos_2)
            face_3 = ImageMobject(clean_arr).match_height(noise_3).move_to(pos_3)

        # 0:22 - 0:35: Crossfade (FadeTransform) từ nhiễu sang ảnh rõ nét
        # Cảm giác ma thuật xuất hiện khi 3 mô hình khác nhau cho ra cùng 1 kết quả
        self.play(
            FadeIn(face_1), FadeOut(noise_1),
            FadeIn(face_2), FadeOut(noise_2),
            FadeIn(face_3), FadeOut(noise_3),
            run_time=5,
            rate_func=linear # Linear để thấy rõ sự biến đổi đều đặn của pixel
        )
        self.wait(8)

        # ---------------------------------------------------------------------
        # [0:35 - 1:05]: Hội tụ 3 ảnh và Tiêu đề "The Phenomenon of Reproducibility"
        # ---------------------------------------------------------------------
        
        # Dòng chữ chính. Vẫn giữ phong cách có chân, in nghiêng sang trọng.
        title = Text(
            '"The Phenomenon of Reproducibility"', 
            font="Times New Roman", 
            slant=ITALIC
        ).scale(0.9)
        
        # 0:35 - 0:37: Xóa bỏ các khung viền và tên mạng để dọn dẹp không gian
        self.play(
            FadeOut(box_1), FadeOut(box_2), FadeOut(box_3),
            FadeOut(label_1), FadeOut(label_2), FadeOut(label_3),
            run_time=2
        )

        # Đặt vị trí chữ ở phía trên, cách tâm màn hình một khoảng vừa đủ
        title.next_to(ORIGIN, UP, buff=2.5)

        # 0:37 - 0:45: Gộp 3 ảnh về trung tâm, phóng to và từ từ hiện dòng chữ
        self.play(
            face_1.animate.move_to(ORIGIN).scale(1.5),
            face_2.animate.move_to(ORIGIN).scale(1.5),
            face_3.animate.move_to(ORIGIN).scale(1.5),
            FadeIn(title, shift=DOWN * 0.5), # Dòng chữ hơi trượt nhẹ từ trên xuống
            run_time=5,
            rate_func=smooth # Gia tốc mượt mà ở hai đầu chuyển động
        )
        
        # 0:45 - 1:05: Dành thời gian nghỉ để thông điệp đọng lại trong tâm trí khán giả
        self.wait(20)