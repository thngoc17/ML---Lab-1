from manim import *
import numpy as np

class NoiseCompassScene(Scene):
    def construct(self):
        # =========================================================
        # [2:20 - 2:45] Forward Process & SDE (Thời lượng: ~25s)
        # Voice: "Để giải mã bí ẩn này... SDE này."
        # =========================================================
        self.next_section("Forward Process")
        self.clear()
        self.wait(1) # Nghỉ một nhịp trước khi bắt đầu

        # 1. Tạo dữ liệu quỹ đạo Brown (Random Walk)
        np.random.seed(42)
        steps = 400
        rw = np.cumsum(np.random.normal(0, 0.12, (steps, 3)), axis=0)
        rw[:, 2] = 0  
        start_pos = UP * 0.5 + LEFT * 1.5
        rw += start_pos
        path_curve = VMobject().set_points_smoothly(rw)

        # 2. Khởi tạo x_0
        x0_dot = Dot(start_pos, color=TEAL, radius=0.08)
        x0_label = MathTex("x_0", color=TEAL).next_to(x0_dot, UP + LEFT, buff=0.1)

        # Hiện x0 khi đọc "Một điểm dữ liệu ban đầu..."
        self.play(FadeIn(x0_dot, scale=0.5), FadeIn(x0_label), run_time=2)
        self.wait(1.5)

        # 3. Phương trình SDE xuất hiện sớm để dẫn dắt
        sde = MathTex(
            "dx", "=", "f(x,t)", "dt", "+", "g(t)", "dw"
        ).scale(1.2).to_edge(UP, buff=1)
        sde.set_color_by_tex("f(x,t)", GREEN_C)
        sde.set_color_by_tex("g(t)", MAROON_C)
        sde.set_color_by_tex("dw", GREY_A)

        self.play(Write(sde), run_time=2.5)
        self.wait(1)

        # 4. Vẽ quỹ đạo (khớp với câu "trôi dạt vô định...")
        tracker = ValueTracker(0)
        traced_path = TracedPath(
            x0_dot.get_center, 
            stroke_width=3, 
            stroke_color=BLUE_C,
            dissipating_time=0.8
        )
        full_path = VMobject().set_points_smoothly(rw).set_stroke(BLUE_E, width=1, opacity=0.3)
        self.add(full_path, traced_path)
        x0_dot.add_updater(lambda m: m.move_to(path_curve.point_from_proportion(tracker.get_value())))

        self.play(
            tracker.animate.set_value(1),
            run_time=12, # Chạy chậm lại để bao phủ hết đoạn thoại
            rate_func=linear
        )
        
        x0_dot.remove_updater(x0_dot.updaters[0])
        xT_label = MathTex("x_T", color=BLUE_B).next_to(x0_dot, RIGHT)
        self.play(FadeIn(xT_label, shift=LEFT*0.3), run_time=1.5)
        self.wait(3.5) # Chờ cho đến hết mốc 2:45

        # =========================================================
        # [2:45 - 3:10] Probability Flow ODE (Thời lượng: ~25s)
        # Voice: "Nhưng vẻ đẹp của toán học... Probability Flow ODE."
        # =========================================================
        self.next_section("Probability Flow ODE")

        ode = MathTex(
            "dx", "=", "\\left[", "f(x,t)", "-", "\\frac{1}{2}", "g(t)", "^2", "\\nabla_x \\log p_t(x)", "\\right]", "dt"
        ).scale(1.2).to_edge(UP, buff=1)
        ode.set_color_by_tex("f(x,t)", GREEN_C)
        ode.set_color_by_tex("g(t)", MAROON_C)
        ode.set_color_by_tex("\\nabla_x \\log p_t(x)", WHITE)

        # Xóa nền khi đọc "Quá trình sinh ảnh thực chất là..."
        self.play(
            FadeOut(traced_path), FadeOut(full_path), 
            FadeOut(x0_dot), FadeOut(x0_label), FadeOut(xT_label),
            run_time=2.5
        )
        self.wait(1.5)

        # Transform mượt mà sang ODE 
        self.play(
            TransformMatchingTex(sde, ode, key_map={
                "f(x,t)": "f(x,t)", "g(t)": "g(t)", "dt": "dt", "dx": "dx", "=": "="
            }),
            run_time=4,
            path_arc=PI/6
        )
        # Để phương trình trên màn hình đủ lâu cho khán giả ngắm nghía trọn vẹn
        self.wait(17) # Chờ cho đến mốc 3:10

        # =========================================================
        # [3:10 - 3:35] Score Function Compass (Thời lượng: ~25s)
        # Voice: "Hãy chú ý vào cụm vi phân này... lời nguyền của chiều dữ liệu?"
        # =========================================================
        self.next_section("Score Function Compass")

        # 1. Nhấn mạnh "La bàn" (Khớp với "Hãy chú ý vào cụm vi phân này...")
        self.play(
            ode.animate.set_color_by_tex("\\nabla_x \\log p_t(x)", YELLOW),
            run_time=2
        )
        self.play(
            Indicate(ode.get_part_by_tex("\\nabla_x \\log p_t(x)"), color=YELLOW, scale_factor=1.15),
            run_time=2
        )
        self.wait(2)

        # Xóa phương trình để chuyển sang Vector Field
        self.play(FadeOut(ode), run_time=2)

        # 2. Xây dựng Data Distribution và Vector Field
        mode1 = np.array([-3.5, -1, 0])
        mode2 = np.array([3.5, 1.5, 0])
        np.random.seed(0)
        pts1 = [mode1 + np.random.normal(0, 0.4, 3) for _ in range(40)]
        pts2 = [mode2 + np.random.normal(0, 0.4, 3) for _ in range(40)]
        for p in pts1 + pts2: p[2] = 0

        data_cloud = VGroup(*[
            Dot(p, color=YELLOW_A, radius=np.random.uniform(0.03, 0.06)).set_opacity(0.8) 
            for p in pts1 + pts2
        ])

        def score_func(pos):
            d1 = pos - mode1
            d2 = pos - mode2
            w1 = np.exp(-0.5 * np.linalg.norm(d1)**2)
            w2 = np.exp(-0.5 * np.linalg.norm(d2)**2)
            total_w = w1 + w2 + 1e-8
            return - (w1 * d1 + w2 * d2) / total_w

        def smooth_length(norm):
            return 0.45 * (2 / (1 + np.exp(-norm)) - 1)

        vector_field = ArrowVectorField(
            score_func, x_range=[-7, 7, 0.7], y_range=[-4, 4, 0.7],
            colors=[BLUE_E, BLUE_C, TEAL, YELLOW_C], length_func=smooth_length
        ).set_opacity(0.85)

        # Hiện trường vector mượt mà (Khớp với "Nó tạo ra một trường vector...")
        self.play(
            AnimationGroup(
                FadeIn(data_cloud, lag_ratio=0.01),
                Create(vector_field, lag_ratio=0.005),
                lag_ratio=0.5
            ),
            run_time=5
        )

        # 3. Minh họa hạt bị hút về (Reverse Process)
        sample_dot = Dot(UP * 3 + LEFT * 5, color=RED, radius=0.1)
        sample_glow = Dot(UP * 3 + LEFT * 5, color=RED, radius=0.25).set_opacity(0.4)
        sample_group = VGroup(sample_glow, sample_dot)
        self.play(FadeIn(sample_group, scale=0.2), run_time=1.5)

        def reverse_step(mob, dt):
            pos = mob.get_center()
            grad = score_func(pos)
            mob.shift(grad * dt * 1.5)

        sample_group.add_updater(reverse_step)
        
        # Chờ hạt di chuyển trong lúc voiceover kết thúc ("...lời nguyền của chiều dữ liệu?")
        self.wait(8)
        
        sample_group.remove_updater(reverse_step)
        self.play(FadeOut(sample_group), FadeOut(vector_field), FadeOut(data_cloud), run_time=2.5)