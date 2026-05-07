# KỊCH BẢN CHI TIẾT - LAB 1 - Intro2ML
Dưới đây là kịch bản chi tiết cho video cho Lab 1 môn Nhập môn học máy. Video dựa trên series bài giảng **Harnessing Low Dimensionality in Diffusion
Models: From Theory to Practice** được trình bày trong hội nghị **ICML** - một trong các hội nghị về AI hàng đầu thế giới.
Kịch bản được chia làm 3 phần:
* Phần 1 - Bài giảng 1 (2:40 - 8:35)

---

## Phần 1: Hình học của sự Khái quát hóa trong Diffusion Models

### Scene 1: Lời ngỏ và Hiện tượng Tái tạo (0:00 - 1:30)
**Mục tiêu:** Đặt vấn đề bằng một hiện tượng trực quan gây tò mò.
**Thời lượng:** 90 giây (khoảng 160 từ).

* **[0:00 - 0:20] Manim Visual:** Màn hình đen (`Scene`). Dùng `ImageMobject` kết hợp `Noise` shader để tạo ra một mảng nhiễu Gaussian $x_T$. Dùng `VGroup` nhân bản mảng nhiễu này thành 3 bản giống hệt nhau, trượt về 3 góc màn hình bằng `ApplyMethod`.
* **[0:20 - 0:50] Manim Visual:** Vẽ 3 `SurroundingRectangle` đại diện cho 3 kiến trúc mạng: U-Net, DiT, và EDM. Từ từ `FadeIn` kết quả đầu ra: cả 3 mạng giải nhiễu mảng nhiễu ban đầu thành 3 bức ảnh hoàn toàn trùng khớp (ví dụ: ảnh một khuôn mặt).
* **[0:50 - 1:30] Manim Visual:** Dùng `Camera` zoom cận cảnh vào một vùng pixel để thấy sự giống nhau tuyệt đối. Hiện dòng chữ bằng `Text(font="CMU Serif")`: *"The Phenomenon of Reproducibility"*.

**[Voiceover]**
*(Nhạc piano ambient nhẹ nhàng)*
"Hãy bắt đầu bằng một thí nghiệm tư duy. Giả sử, bạn lấy một mảng nhiễu trắng ngẫu nhiên... và cung cấp nó cho ba mô hình Diffusion có kiến trúc hoàn toàn khác biệt. Một mạng U-Net cổ điển, một Transformer hiện đại, và một mô hình được tối ưu bằng một bộ tham số độc lập.
Trực giác có thể mách bảo ta rằng, từ một khởi đầu hỗn độn, mỗi mạng nơ-ron sẽ 'ảo giác' ra một kết quả khác nhau. Nhưng thực tế lại phơi bày một hiện tượng kỳ lạ: Bằng một cơ chế ẩn nào đó, cả ba mô hình đều hội tụ về chung một bức ảnh duy nhất, trùng khớp đến từng điểm ảnh.
Trong giới nghiên cứu, điều này được gọi là hiện tượng tái tạo — Reproducibility. Nó là minh chứng cho thấy các mạng nơ-ron sâu không hề học vẹt một cách ngẫu nhiên. Thay vào đó, chúng đang cùng nhau chia sẻ một quỹ đạo hình học ẩn giấu nào đó."

### Scene 2: La bàn trong không gian nhiễu (1:30 - 3:00)
**Mục tiêu:** Nhắc lại toán học cốt lõi (SDE, ODE, Score function).
**Thời lượng:** 90 giây (khoảng 170 từ).

* **[1:30 - 2:00] Manim Visual:** Xóa cảnh cũ. Đặt một `Dot` đại diện cho $x_0$. Dùng một `ValueTracker` kết hợp `TracedPath` để vẽ một quỹ đạo chuyển động Brown hỗn loạn (Forward process) biến $x_0$ thành $x_T$. Dùng `MathTex` hiện phương trình: $dx = f(x,t)dt + g(t)dw$.
* **[2:00 - 2:30] Manim Visual:** Dùng `TransformMatchingTex` biến đổi mượt mà SDE thuận thành ODE lùi (Probability Flow ODE). Giữ nguyên các ký tự chung để tạo sự liên kết thị giác:
    $$dx = \left[ f(x, t) - \frac{1}{2}g(t)^2 \nabla_x \log p_t(x) \right] dt$$
* **[2:30 - 3:00] Manim Visual:** Dùng `set_color` tô vàng cụm $\nabla_x \log p_t(x)$. Chuyển cảnh sang một `VectorField`, trong đó các vector gradient đều hướng về các điểm dữ liệu mật độ cao.

**[Voiceover]**

"Để giải mã bí ẩn này, hãy nhìn lại gốc rễ của quá trình khuếch tán. Một điểm dữ liệu ban đầu sẽ trải qua một quá trình tản mạn ngẫu nhiên, trôi dạt vô định theo phương trình vi phân ngẫu nhiên, hay SDE này.
Nhưng vẻ đẹp của toán học nằm ở tính khả nghịch. Quá trình sinh ảnh thực chất là việc đi ngược lại quỹ đạo đó, tuân theo một phương trình vi phân thường — Probability Flow ODE. 
Hãy chú ý vào cụm vi phân này: Score Function. Trong một không gian mênh mông nhiễu loạn, đại lượng này chính là một chiếc la bàn. Nó tạo ra một trường vector, luôn chỉ hướng về nơi có mật độ dữ liệu thực cao nhất. 
Mục tiêu duy nhất của mạng nơ-ron là xấp xỉ chiếc la bàn này. Nhưng vấn đề là: không gian hình ảnh chứa hàng triệu chiều. Làm sao một mô hình có thể xấp xỉ chính xác một trường vector bao la đến vậy mà không dính phải lời nguyền của chiều dữ liệu?"

### Scene 3: Phước lành của cấu trúc chiều thấp (3:00 - 4:30)
**Mục tiêu:** Đưa ra giả định MoLRG để giải quyết Curse of Dimensionality.
**Thời lượng:** 90 giây (khoảng 165 từ).

* **[3:00 - 3:30] Manim Visual:** Dùng `ThreeDAxes` xoay một không gian 3D rộng lớn. Rải vài `Dot3D` lơ lửng, cách xa nhau. Hiện chữ "Curse of Dimensionality".
* **[3:30 - 4:00] Manim Visual:** Camera xoay góc. Bất ngờ hiện ra một `ParametricSurface` 2D mỏng manh đi qua tất cả các điểm đó. Các điểm này thực chất nằm trọn trên mặt phẳng này. Hiện chữ "Intrinsic Dimension $r \ll d$".
* **[4:00 - 4:30] Manim Visual:** Dùng `MathTex` hiện công thức phân phối hỗn hợp Gauss hạng thấp:
    $$p_{data}(x) = \frac{1}{K} \sum_{i=1}^K \mathcal{N}(x; 0, U_i U_i^T)$$
    Vẽ các hệ vector cơ sở $U_1, U_2$ ngay trên mặt phẳng để minh họa không gian con.

**[Voiceover]**
"Nếu dữ liệu lấp đầy mọi ngóc ngách của không gian vật lý, ta sẽ cần một lượng mẫu khổng lồ, tăng theo hàm mũ của số chiều. 
May mắn thay, dữ liệu thực tế mang đến một 'phước lành'. Một bức ảnh không phải là tập hợp pixel ngẫu nhiên, chúng bị ràng buộc bởi hình khối và ánh sáng. Toàn bộ kho tàng hình ảnh tự nhiên, trên thực tế, lại cư ngụ trên những không gian con có số chiều nội tại cực kỳ nhỏ.
Trong ngôn ngữ toán học, ta có thể mô phỏng cấu trúc này bằng một Hỗn hợp Gauss hạng thấp, gọi là MoLRG. Thay vì là một đám mây khối cầu khổng lồ trong không gian $d$ chiều, dữ liệu thực chất tụ tập lại quanh những mặt phẳng mỏng manh $U_i$. Nhiệm vụ của quá trình học không còn là lấp đầy không gian bao la, mà là định vị được các mặt phẳng này."


### Scene 4: Phép chiếu Hình học và Sự tương đương với PCA (4:30 - 6:00)
*Mục tiêu: Dùng trực giác của phép chiếu (projection) để giải thích PCA và hiện tượng chuyển pha.*
*Thời lượng: 90 giây (182 từ).*

**[4:30 - 5:00] Manim Visual:** Đưa màn hình về 2D. Viết hàm mục tiêu khử nhiễu quen thuộc: $\min_\theta \mathbb{E} \left[ ||\epsilon - s_\theta(x_t, t)||^2 \right]$. [cite_start]Sử dụng `TransformMatchingTex` biến đổi hàm này qua lăng kính công thức Tweedie, làm nổi bật thông điệp: Việc đoán nhiễu (Score) thực chất là mạng đang cố gắng ước lượng lại ảnh gốc $\mathbb{E}[x_0|x_t]$.

**[5:00 - 5:30] Manim Visual:** Mở ra không gian 3D. Vẽ một mặt phẳng 2D trong suốt (đại diện cho không gian con $U$) và một điểm nhiễu $x_t$ lơ lửng bên trên. Dùng `DashedLine` chiếu vuông góc điểm $x_t$ xuống mặt phẳng để tạo ra điểm $\hat{x}_0$. Hiện công thức chiếu: $\hat{x}_0 = U U^T x_t$. Sau đó dùng `Transform` biến bài toán nơ-ron thành PCA: $\max_U ||UX||_F^2 \quad \text{s.t.} \quad U^T U = I$.

**[5:30 - 6:00] Manim Visual:** Mở ra một `Axes` 2D. Trục hoành là lượng dữ liệu log $\log_2(N/ID)$, trục tung là khả năng khái quát. [cite_start]Dùng `UpdateFromAlphaFunc` vẽ một đường cong nằm ngang sát đáy, đến một ngưỡng (threshold $N > c \cdot ID$) thì vọt thẳng lên cao (Generalization Phase).

**[Voiceover]**
"Vậy mạng nơ-ron học các mặt phẳng này như thế nào? Lời giải nằm ở công thức Tweedie. Công thức này chứng minh rằng: tối ưu hàm đoán nhiễu của quá trình Diffusion... thực chất là ta đang cố gắng ước lượng lại bức ảnh gốc.


Về mặt hình học, nếu dữ liệu cư ngụ trên một mặt phẳng, cách tốt nhất để khử nhiễu là chiếu vuông góc điểm nhiễu đó xuống mặt phẳng. Toán học chỉ ra rằng, mạng nơ-ron lúc này hoạt động chính xác như một phép chiếu tuyến tính với ma trận $UU^T$. Nhờ vậy, hàm loss phức tạp của mạng Deep Learning bỗng chốc thu gọn thành bài toán Phân tích thành phần chính — PCA. Mô hình đang tự xoay ma trận $U$ để bao trọn lấy nhiều dữ liệu nhất có thể.

Sự tương đương này dẫn đến một hiện tượng chuyển pha vật lý ngoạn mục. Lượng ảnh cần để huấn luyện không phụ thuộc vào số pixel, mà tỷ lệ thuận với số chiều nội tại của dữ liệu. Chỉ khi vượt qua ngưỡng này, mô hình mới bừng tỉnh, phá vỡ trạng thái học vẹt để tiến thẳng vào vùng Khái quát hóa."

### Scene 5: Định lượng qua Probability Flow Distance (6:00 - 7:30)
**Mục tiêu:** Giới thiệu PFD làm thước đo.
**Thời lượng:** 90 giây (khoảng 160 từ).

* **[6:00 - 6:30] Manim Visual:** Chia đôi màn hình. Nửa trái: Mô hình Teacher (đại diện $p_{\theta^*}$). Nửa phải: Mô hình Student (đại diện $p_\theta$).
* **[6:30 - 7:00] Manim Visual:** Vẽ 2 quỹ đạo đường cong (ODE trajectory) chạy song song từ cùng một mảng nhiễu $x_T$ về tâm. 
* **[7:00 - 7:30] Manim Visual:** Dùng `MathTex` hiện công thức PFD, đồng thời vẽ các đường `DashedLine` nối sự chênh lệch giữa hai điểm cuối của 2 quỹ đạo.
    $$PFD(p_\theta, p_{\theta^*}) = \mathbb{E}_{x \sim \mathcal{N}(0, T^2I)} \left[ ||\Phi_{p_\theta}(x_T) - \Phi_{p_{\theta^*}}(x_T)||^2 \right]$$

**[Voiceover]**
"Tuy nhiên, làm sao để đo lường định lượng sự khái quát này, khi ta vĩnh viễn không biết được phân phối thực của tự nhiên? 
Giải pháp là thiết lập một hệ quy chiếu: Ta dùng một mô hình Teacher đóng vai trò là chân lý tạo ra dữ liệu, và một mô hình Student học từ lượng dữ liệu đó. 
Thay vì đếm pixel hay dùng các thang đo như FID, ta đo lường khoảng cách giữa các quỹ đạo động lực học thông qua Probability Flow Distance — viết tắt là PFD. Thước đo này tính toán chuẩn bình phương sự sai lệch giữa điểm đích mà quỹ đạo ODE của Student đạt đến, so với quỹ đạo chuẩn xác của Teacher, khi cả hai cùng xuất phát từ một điểm nhiễu $x_T$."

### Scene 6: Động lực học Học tập và Hiện tượng Đổ đèo kép (7:30 - 9:00)
**Mục tiêu:** Đưa ra khái niệm Double Descent.
**Thời lượng:** 90 giây (khoảng 150 từ).

* **[7:30 - 8:00] Manim Visual:** Xóa toàn bộ. Vẽ một `Axes` biểu diễn quá trình huấn luyện. Trục hoành: Số Epochs. Trục tung: Lỗi khái quát hóa (Generalization Error - đo bằng PFD).
* **[8:00 - 8:40] Manim Visual:** Bắt đầu vẽ đường cong huấn luyện. Đường cong đi xuống đều... rồi đột ngột vòng lên tạo thành một đỉnh chóp sắc nhọn... sau đó tiếp tục đổ dốc (Descent) cắm xuống vùng cực tiểu ổn định. 
* **[8:40 - 9:00] Manim Visual:** Dùng các mũi tên chỉ vào chóp nhọn, ghi chú "High Variance" (Màu đỏ) và "Low Bias" (Màu xanh). Hiện cụm từ "Epoch-wise Double Descent". Dừng hình.

**[Voiceover]**
"Khi quan sát sự tiến hóa của khoảng cách PFD xuyên suốt quá trình huấn luyện, ta bắt gặp một hành vi vật lý đầy tính nghịch lý: Hiện tượng đổ đèo kép — Double Descent.
Ở những Epoch đầu tiên, lỗi giảm dần do mô hình cố gắng ghi nhớ dữ liệu. Nhưng sau đó, đường cong đột ngột tăng vọt lên, phá vỡ mọi sự ổn định. Đây là khoảnh khắc mô hình rơi vào cuộc chiến khốc liệt nhất giữa Phương sai và Độ chệch (Bias-Variance Tradeoff) khi phải xấp xỉ một không gian quá lớn.
Nhưng, nếu ta kiên nhẫn huấn luyện xuyên qua 'cơn bão' này, mô hình sẽ tự tái cấu trúc, bước vào lần đổ đèo thứ hai, và hội tụ vĩnh viễn về quỹ đạo hình học chuẩn xác nhất của dữ liệu."

