from manim import *
import numpy as np

class QuantitativeMetrics(Scene):
    def construct(self):
        # ==========================================================
        # [1:05 - 1:30] PHẦN 1: CNN & TRÍCH XUẤT ĐẶC TRƯNG
        # ==========================================================
        
        # 1. Khởi tạo ảnh gốc với scale chính xác như cuối phân cảnh 1.1 (height = 3.6)
        try:
            base_img = ImageMobject("raw_media/cat.jpeg")
            base_img.height = 3.6
            base_img.move_to(ORIGIN)
        except:
            # Ảnh giả lập nếu thiếu file
            clean_arr = np.zeros((100, 100, 3), dtype=np.uint8)
            clean_arr[:, :, 0] = np.linspace(0, 255, 100).reshape(1, 100)
            clean_arr[:, :, 1] = np.linspace(255, 0, 100).reshape(100, 1)
            base_img = ImageMobject(clean_arr)
            base_img.height = 3.6
            base_img.move_to(ORIGIN)

        self.add(base_img)
        self.wait(1)

        # Tạo 2 bản sao đại diện cho 2 model
        img1 = base_img.copy()
        img2 = base_img.copy()

        # 2. Tách ảnh ra 2 nhánh mượt mà và trả về kích thước gốc ở 1.1 (height = 2.4)
        pos_1 = LEFT * 5 + UP * 1.8
        pos_2 = LEFT * 5 + DOWN * 1.8

        self.play(
            img1.animate.set_height(2.4).move_to(pos_1),
            img2.animate.set_height(2.4).move_to(pos_2),
            FadeOut(base_img),
            run_time=2
        )
        
        # 3. Tạo khung Model bằng Rectangle
        box_1 = Rectangle(width=img1.width + 0.2, height=img1.height + 0.2, color=TEAL).set_stroke(width=3).move_to(img1.get_center())
        box_2 = Rectangle(width=img2.width + 0.2, height=img2.height + 0.2, color=MAROON).set_stroke(width=3).move_to(img2.get_center())

        label_unet = Tex("U-Net").scale(0.8).next_to(box_1, UP)
        label_dit = Tex("DiT").scale(0.8).next_to(box_2, UP)

        self.play(
            Create(box_1), Write(label_unet),
            Create(box_2), Write(label_dit)
        )
        self.wait(1)

        # 4. Tạo khối CNN (SSCD)
        cnn_box = VGroup(
            Rectangle(height=5, width=2, stroke_color=GREY_B, fill_color=DARK_GREY, fill_opacity=0.8),
            NumberPlane(x_range=[-1, 1, 0.5], y_range=[-2.5, 2.5, 0.5], background_line_style={"stroke_opacity": 0.3})
        ).move_to(LEFT * 1)
        
        # Đưa Label SSCD Network lên trên đỉnh lưới vuông
        cnn_label = VGroup(Tex("SSCD"), Tex("Network")).arrange(DOWN).scale(0.7).set_color(YELLOW)
        cnn_label.next_to(cnn_box, UP, buff=0.2)
        
        self.play(DrawBorderThenFill(cnn_box), Write(cnn_label))
        
        # 5. Hút ảnh và khung vào CNN
        self.play(
            img1.animate.scale(0.2).move_to(cnn_box.get_left() + UP*1.5).set_opacity(0),
            img2.animate.scale(0.2).move_to(cnn_box.get_left() + DOWN*1.5).set_opacity(0),
            FadeOut(box_1), FadeOut(box_2),
            FadeOut(label_unet), FadeOut(label_dit),
            run_time=1.5,
            rate_func=rush_into
        )

        # 6. Hiển thị Vector đầu ra phát sáng
        def create_glowing_vector(values, color, position):
            matrix = Matrix(values).scale(0.6).move_to(position)
            matrix.set_color(color)
            glow = matrix.copy().set_opacity(0.3).set_stroke(width=8, color=color)
            return VGroup(glow, matrix)

        vec1 = create_glowing_vector([["0.85"], ["-0.21"], [r"\vdots"], ["0.54"]], BLUE_B, RIGHT * 2 + UP * 1.5)
        vec2 = create_glowing_vector([["0.82"], ["-0.19"], [r"\vdots"], ["0.60"]], TEAL_B, RIGHT * 2 + DOWN * 1.5)
        
        vec1_label = MathTex(r"h(x_1)", color=BLUE_B).next_to(vec1, RIGHT)
        vec2_label = MathTex(r"h(x_2)", color=TEAL_B).next_to(vec2, RIGHT)

        self.play(FadeIn(vec1, shift=RIGHT), FadeIn(vec2, shift=RIGHT), Write(vec1_label), Write(vec2_label))
        self.wait(1)

        # 7. Hiện công thức Cosine Similarity
        formula = MathTex(
            r"\mathcal{M}_{SSCD}(x_1, x_2) := \frac{|\langle h(x_1), h(x_2) \rangle|}{||h(x_1)||_2 \cdot ||h(x_2)||_2}",
            font_size=36
        )
        formula.next_to(cnn_label, RIGHT, buff=0.8).align_to(cnn_label, UP)

        self.play(Write(formula))
        self.wait(3)

        # ==========================================================
        # CHUYỂN CẢNH: RP SCORE TRƯỚC KHI VẼ ĐỒ THỊ
        # ==========================================================
        
        # 1. Gom nhóm TOÀN BỘ các đối tượng của phần SSCD và xóa sạch 1 lần duy nhất
        part1_group = VGroup(cnn_box, cnn_label, vec1, vec2, vec1_label, vec2_label, formula)
        self.play(FadeOut(part1_group))

        # 2. Hiện RP Score ở giữa màn hình (Cảnh mới hoàn toàn trống)
        rp_title = Tex("RP Score (Reproducibility)", color=RED).scale(1.2).move_to(ORIGIN)
        self.play(Write(rp_title))
        self.wait(2)

        # 3. Thu nhỏ và đưa về góc trái để làm tiêu đề cho đồ thị
        self.play(rp_title.animate.to_corner(UL).scale(0.7))

        # ==========================================================
        # [1:30 - 2:20] PHẦN 2: ĐỒ THỊ VÀ LEGEND TIÊU CHUẨN
        # ==========================================================
        
        # 1. Tạo hệ trục tọa độ (Axes)
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 1.2, 0.2],
            x_length=8,
            y_length=5,
            axis_config={"color": WHITE, "include_tip": True},
        ).shift(DOWN * 0.5)
        
        x_label = axes.get_x_axis_label(r"N \text{ (Training Size)}", edge=DOWN, direction=DOWN)
        y_label = axes.get_y_axis_label(r"\text{Score}", edge=LEFT, direction=LEFT)
        
        self.play(Create(axes), Write(x_label), Write(y_label))

        # 2. Chia vùng đồ thị
        mem_region = axes.get_area(axes.plot(lambda x: 1.2, x_range=[0, 5]), color=BLUE_E, opacity=0.15)
        mem_label = VGroup(Tex("Memorization"), Tex("Regime")).arrange(DOWN).scale(0.5).set_color(BLUE_C)
        mem_label.move_to(axes.c2p(2.5, 1.05))
        
        gen_region = axes.get_area(axes.plot(lambda x: 1.2, x_range=[5, 10]), color=YELLOW_E, opacity=0.15)
        gen_label = VGroup(Tex("Generalization"), Tex("Regime")).arrange(DOWN).scale(0.5).set_color(YELLOW_C)
        gen_label.move_to(axes.c2p(7.5, 1.05))

        self.play(FadeIn(mem_region), Write(mem_label))
        self.play(FadeIn(gen_region), Write(gen_label))

        # 3. Vẽ đường cong RP Score
        rp_curve = axes.plot(lambda x: 0.03 * (x - 5)**2 + 0.2, x_range=[0.5, 9.5], color=RED)
        self.play(Create(rp_curve, run_time=3))

        # 4. Vẽ đường cong GL Score
        gl_curve = axes.plot(lambda x: 0.9 / (1 + np.exp(-2 * (x - 7.5))), x_range=[0.5, 9.5], color=GREEN)
        self.play(Create(gl_curve, run_time=3))

        # 5. Tạo Legend Box
        gl_leg_line = Line(ORIGIN, RIGHT * 0.5, color=GREEN, stroke_width=4)
        gl_leg_text = Tex("GL Score", color=GREEN).scale(0.6)
        gl_leg = VGroup(gl_leg_line, gl_leg_text).arrange(RIGHT, buff=0.2)

        rp_leg_line = Line(ORIGIN, RIGHT * 0.5, color=RED, stroke_width=4)
        rp_leg_text = Tex("RP Score", color=RED).scale(0.6)
        rp_leg = VGroup(rp_leg_line, rp_leg_text).arrange(RIGHT, buff=0.2)

        legend = VGroup(gl_leg, rp_leg).arrange(DOWN, aligned_edge=LEFT)
        
        # Đặt legend nằm ngoài phía bên phải của hệ trục tọa độ
        legend.next_to(axes, RIGHT, buff=0.3).set_y(axes.c2p(10, 0.9)[1])

        self.play(FadeIn(legend))
        self.wait(3)

        # 6. Group toàn bộ đồ thị lại và bung dấu chấm hỏi
        graph_group = VGroup(
            axes, x_label, y_label,
            mem_region, mem_label, gen_region, gen_label,
            rp_curve, gl_curve, legend, rp_title
        )

        question_mark = Tex("?", color=YELLOW).scale(4).move_to(ORIGIN)
        
        # Xóa TOÀN BỘ đồ thị (bao gồm cả chữ RP Score) và hiện dấu ? ở chính giữa
        self.play(
            FadeOut(graph_group),
            Write(question_mark)
        )
        self.play(Wiggle(question_mark, scale_value=1.2, rotation_angle=0.05 * TAU, run_time=2))
        
        self.wait(2)