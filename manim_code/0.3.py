from manim import *

class TheRecreationPhenomenon(Scene):
    def construct(self):
        # 1. THIẾT LẬP MÀU SẮC ĐẶC TRƯNG
        UNET_COLOR = BLUE_C
        TRANSFORMER_COLOR = TEAL_C
        NOISE_COLOR = GREY_B
        MAP_COLOR = YELLOW_D

        # Lưới nền (Bản đồ hình học ẩn) - Ẩn lúc đầu
        hidden_map = NumberPlane(
            background_line_style={
                "stroke_color": MAP_COLOR,
                "stroke_width": 1.5,
                "stroke_opacity": 0.2
            }
        ).set_z_index(-1)

        # --- [1:45 - 2:10] AUDIO: Gieo xúc xắc / Sự ngẫu nhiên ---
        noise_text = Text("Pure Noise", font_size=24, color=NOISE_COLOR)
        noise_core = Dot(color=WHITE, radius=0.15)
        noise_glow = Dot(color=WHITE, radius=0.6, fill_opacity=0.15)
        
        noise_group = VGroup(noise_glow, noise_core, noise_text).arrange(DOWN, buff=0.2)
        noise_group.move_to(LEFT * 5)

        self.play(FadeIn(noise_group, shift=RIGHT), run_time=2)
        self.wait(1.5)

        # --- [2:10 - 2:25] AUDIO: Hai mô hình hoàn toàn khác nhau ---
        unet_box = RoundedRectangle(corner_radius=0.2, height=1.2, width=3, color=UNET_COLOR, fill_opacity=0.05)
        unet_label = Text("U-Net", font_size=32, color=UNET_COLOR) 
        unet_group = VGroup(unet_box, unet_label).move_to(UP * 2)

        transformer_box = RoundedRectangle(corner_radius=0.2, height=1.2, width=3, color=TRANSFORMER_COLOR, fill_opacity=0.05)
        transformer_label = Text("Transformer", font_size=32, color=TRANSFORMER_COLOR)
        transformer_group = VGroup(transformer_box, transformer_label).move_to(DOWN * 2)

        self.play(
            DrawBorderThenFill(unet_box), Write(unet_label),
            DrawBorderThenFill(transformer_box), Write(transformer_label),
            run_time=2
        )

        path_in_unet = CurvedArrow(noise_group.get_top(), unet_group.get_left(), angle=-TAU/6, color=UNET_COLOR)
        path_in_trans = CurvedArrow(noise_group.get_bottom(), transformer_group.get_left(), angle=TAU/6, color=TRANSFORMER_COLOR)

        self.play(Create(path_in_unet), Create(path_in_trans), run_time=2)
        self.wait(1)

        # --- [2:25 - 2:40] AUDIO: Xuyên qua biển nhiễu loạn và hội tụ ---
        # Đã thay VGroup bằng Group để chứa các ImageMobject
        cat_img_1 = ImageMobject("raw_media/cat.jpeg").scale(0.3)
        cat_img_2 = ImageMobject("raw_media/cat.jpeg").scale(0.3)

        # Xếp ảnh dọc để đồng bộ với layout của U-Net/Transformer
        cat_group = Group(cat_img_1, cat_img_2).arrange(DOWN, buff=0.2).move_to(RIGHT * 4.5)

        # Căn mũi tên đâm thẳng vào tâm cạnh trái của từng ảnh
        path_out_unet = CurvedArrow(unet_group.get_right(), cat_img_1.get_left(), angle=-TAU/6, color=UNET_COLOR)
        path_out_trans = CurvedArrow(transformer_group.get_right(), cat_img_2.get_left(), angle=TAU/6, color=TRANSFORMER_COLOR)

        self.play(Create(path_out_unet), Create(path_out_trans), run_time=2.5)
        self.play(FadeIn(cat_group, scale=0.8), run_time=1.5)

        # --- LỜI GIẢI THÍCH DUY NHẤT: BẢN ĐỒ HÌNH HỌC ẨN ---
        self.play(
            Create(hidden_map, lag_ratio=0.05),
            noise_glow.animate.scale(1.5).set_color(MAP_COLOR),
            run_time=3
        )
        self.wait(2)