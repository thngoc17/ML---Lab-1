# KỊCH BẢN CHI TIẾT - LAB 1 - Intro2ML
Dưới đây là kịch bản chi tiết cho video cho Lab 1 môn Nhập môn học máy. Video dựa trên series bài giảng **Harnessing Low Dimensionality in Diffusion
Models: From Theory to Practice** được trình bày trong hội nghị **ICML** - một trong các hội nghị về AI hàng đầu thế giới.
Kịch bản được chia làm 3 phần:
* Phần 1 - Bài giảng 1 
* Phần 2 - Bài giảng 2
* Phần 3 - Bài giảng 3
---

## Phần 1: Hình học của sự Khái quát hóa trong Diffusion Models

### Scene 1: Lời ngỏ và Hiện tượng Tái tạo (0:00 - 1:05)
**Mục tiêu:** Đặt vấn đề bằng một hiện tượng trực quan gây tò mò.
**Thời lượng:** 90 giây (khoảng 160 từ).

* **[0:00 - 0:15] Manim Visual:** Màn hình đen (`Scene`). Dùng `ImageMobject` kết hợp `Noise` shader để tạo ra một mảng nhiễu Gaussian $x_T$. Dùng `VGroup` nhân bản mảng nhiễu này thành 3 bản giống hệt nhau, trượt về 3 góc màn hình bằng `ApplyMethod`.
* **[0:15 - 0:35] Manim Visual:** Vẽ 3 `SurroundingRectangle` đại diện cho 3 kiến trúc mạng: U-Net, DiT, và EDM. Từ từ `FadeIn` kết quả đầu ra: cả 3 mạng giải nhiễu mảng nhiễu ban đầu thành 3 bức ảnh hoàn toàn trùng khớp (ví dụ: ảnh một khuôn mặt).
* **[0:35 - 1:05] Manim Visual:** Dùng `Camera` zoom cận cảnh vào một vùng pixel để thấy sự giống nhau tuyệt đối. Hiện dòng chữ bằng `Text(font="CMU Serif")`: *"The Phenomenon of Reproducibility"*.

**[Voiceover]**
*(Nhạc piano ambient nhẹ nhàng)*
"Hãy bắt đầu bằng một thí nghiệm tư duy. Giả sử, bạn lấy một mảng nhiễu trắng ngẫu nhiên... và cung cấp nó cho ba mô hình Diffusion có kiến trúc hoàn toàn khác biệt. Một mạng U-Net cổ điển, một Transformer hiện đại, và một mô hình được tối ưu bằng một bộ tham số độc lập.
Trực giác có thể mách bảo ta rằng, từ một khởi đầu hỗn độn, mỗi mạng nơ-ron sẽ 'ảo giác' ra một kết quả khác nhau. Nhưng thực tế lại phơi bày một hiện tượng kỳ lạ: Bằng một cơ chế ẩn nào đó, cả ba mô hình đều hội tụ về chung một bức ảnh duy nhất, trùng khớp đến từng điểm ảnh.
Trong giới nghiên cứu, điều này được gọi là hiện tượng tái tạo — Reproducibility. Nó là minh chứng cho thấy các mạng nơ-ron sâu không hề học vẹt một cách ngẫu nhiên. Thay vào đó, chúng đang cùng nhau chia sẻ một quỹ đạo hình học ẩn giấu nào đó."


---

### Scene 2: Thước đo Định lượng và Nghịch lý Hai trạng thái (1:05 - 2:20)
*Mục tiêu: Đưa toán học vào đo lường hiện tượng (SSCD, Cosine Similarity) và bóc tách ranh giới giữa Học vẹt (Memorization) và Khái quát hóa (Generalization).*
*Thời lượng: 90 giây (khoảng 175 từ).*

**[1:05 - 1:30] Manim Visual:** Từ 3 bức ảnh trùng khớp ở Scene 1, giữ lại 2 ảnh ($x_1, x_2$). Dùng `Transform` biến một khối hộp lưới (đại diện cho mạng CNN trích xuất đặc trưng - SSCD) hút 2 bức ảnh này vào. Ở đầu ra, hiện hai hệ vector $h(x_1)$ và $h(x_2)$ phát sáng lơ lửng.
Dùng `MathTex` hiện công thức Cosine Similarity:


$$\mathcal{M}_{SSCD}(x_1, x_2) := \frac{|\langle h(x_1), h(x_2) \rangle|}{||h(x_1)||_2 \cdot ||h(x_2)||_2}$$

Và định nghĩa thước đo tái tạo **RP Score** (Reproducibility Score).

**[1:30 - 1:55] Manim Visual:** Xóa phương trình, mở ra một `Axes` 2D. Trục hoành là Kích thước tập dữ liệu huấn luyện ($N$). Trục tung là Điểm số.
Vẽ đường cong **RP Score** (màu đỏ). Đường này bắt đầu ở mức rất cao, sau đó võng xuống tạo thành hình chữ U, rồi lại tăng vọt lên ở cuối trục hoành. Chia đồ thị thành 2 vùng mờ: Bên trái là "Memorization Regime" (Vùng Học vẹt), bên phải là "Generalization Regime" (Vùng Khái quát hóa).

**[1:55 - 2:20] Manim Visual:** Để giải thích sự khác biệt của 2 đỉnh chữ U, vẽ thêm đường cong **GL Score** (Generalization Score - độ sai khác so với tập dữ liệu gốc). Đường GL ở bên trái nằm bẹp ở mức 0 (trùng khớp với data gốc), nhưng ở bên phải lại vọt lên cao cùng với RP. Cảnh kết thúc bằng dấu chấm hỏi lớn lơ lửng trên vùng Khái quát hóa.

**[Voiceover]**
"Nhưng trong khoa học máy tính, mắt thường là chưa đủ. Để chứng minh sự hội tụ này, các nhà nghiên cứu đưa các bức ảnh qua một mạng trích xuất đặc trưng chuyên dụng, gọi là SSCD. Bằng cách tính độ tương đồng Cosine giữa các vector đặc trưng này , họ định nghĩa ra một xác suất gọi là Điểm số Tái tạo – RP Score.

Thử nghiệm đo lường RP Score theo lượng dữ liệu huấn luyện đã hé lộ một hành vi cực kỳ thú vị: Đồ thị hình chữ U. Sự tái tạo xảy ra mạnh mẽ ở hai đầu cực đoan!

Nhưng bản chất của chúng hoàn toàn khác nhau. Bằng cách đo thêm điểm số Khái quát hóa – GL Score – tức là so sánh ảnh sinh ra với tập dữ liệu gốc , ta thấy ở vùng bên trái, khi dữ liệu khan hiếm, mô hình chỉ đơn giản là 'học vẹt' và copy y hệt ảnh gốc.
Tuy nhiên, khi lượng dữ liệu đủ lớn tiến vào vùng bên phải, GL Score tăng vọt. Mô hình không còn chép bài nữa. Nó tự tổng hợp ra những bức ảnh hoàn toàn mới. Thế nhưng, các kiến trúc mạng nơ-ron khác nhau vẫn đồng lòng sinh ra chung một kết quả. Khởi đi từ một mảng nhiễu, điều gì đã đóng vai trò làm 'la bàn' dẫn lối cho chúng?"

---

### Scene 3: La bàn trong không gian nhiễu (2:20 - 3:35)
**Mục tiêu:** Nhắc lại toán học cốt lõi (SDE, ODE, Score function).
**Thời lượng:** 90 giây (khoảng 170 từ).

* **[2:20 - 2:45] Manim Visual:** Xóa cảnh cũ. Đặt một `Dot` đại diện cho $x_0$. Dùng một `ValueTracker` kết hợp `TracedPath` để vẽ một quỹ đạo chuyển động Brown hỗn loạn (Forward process) biến $x_0$ thành $x_T$. Dùng `MathTex` hiện phương trình: $dx = f(x,t)dt + g(t)dw$.
* **[2:45 - 3:10] Manim Visual:** Dùng `TransformMatchingTex` biến đổi mượt mà SDE thuận thành ODE lùi (Probability Flow ODE). Giữ nguyên các ký tự chung để tạo sự liên kết thị giác:
    $$dx = \left[ f(x, t) - \frac{1}{2}g(t)^2 \nabla_x \log p_t(x) \right] dt$$
* **[3:10 - 3:35] Manim Visual:** Dùng `set_color` tô vàng cụm $\nabla_x \log p_t(x)$. Chuyển cảnh sang một `VectorField`, trong đó các vector gradient đều hướng về các điểm dữ liệu mật độ cao.

**[Voiceover]**

"Để giải mã bí ẩn này, hãy nhìn lại gốc rễ của quá trình khuếch tán. Một điểm dữ liệu ban đầu sẽ trải qua một quá trình tản mạn ngẫu nhiên, trôi dạt vô định theo phương trình vi phân ngẫu nhiên, hay SDE này.
Nhưng vẻ đẹp của toán học nằm ở tính khả nghịch. Quá trình sinh ảnh thực chất là việc đi ngược lại quỹ đạo đó, tuân theo một phương trình vi phân thường — Probability Flow ODE. 
Hãy chú ý vào cụm vi phân này: Score Function. Trong một không gian mênh mông nhiễu loạn, đại lượng này chính là một chiếc la bàn. Nó tạo ra một trường vector, luôn chỉ hướng về nơi có mật độ dữ liệu thực cao nhất. 
Mục tiêu duy nhất của mạng nơ-ron là xấp xỉ chiếc la bàn này. Nhưng vấn đề là: không gian hình ảnh chứa hàng triệu chiều. Làm sao một mô hình có thể xấp xỉ chính xác một trường vector lớn như vậy mà không dính phải lời nguyền của chiều dữ liệu?"

### Scene 4: Phước lành của cấu trúc chiều thấp (3:35 - 4:45)
**Mục tiêu:** Đưa ra giả định MoLRG để giải quyết Curse of Dimensionality.
**Thời lượng:** 90 giây (khoảng 165 từ).

* **[3:35 - 3:55] Manim Visual:** Dùng `ThreeDAxes` xoay một không gian 3D rộng lớn. Rải vài `Dot3D` lơ lửng, cách xa nhau. Hiện chữ "Curse of Dimensionality".
* **[3:55 - 4:20] Manim Visual:** Camera xoay góc. Bất ngờ hiện ra một `ParametricSurface` 2D mỏng manh đi qua tất cả các điểm đó. Các điểm này thực chất nằm trọn trên mặt phẳng này. Hiện chữ "Intrinsic Dimension $r \ll d$".
* **[4:20 - 4:45] Manim Visual:** Dùng `MathTex` hiện công thức phân phối hỗn hợp Gauss hạng thấp:
    $$p_{data}(x) = \frac{1}{K} \sum_{i=1}^K \mathcal{N}(x; 0, U_i U_i^T)$$
    Vẽ các hệ vector cơ sở $U_1, U_2$ ngay trên mặt phẳng để minh họa không gian con.

**[Voiceover]**
"Nếu dữ liệu lấp đầy mọi ngóc ngách của không gian vật lý, ta sẽ cần một lượng mẫu khổng lồ, tăng theo hàm mũ của số chiều. 
May mắn thay, dữ liệu thực tế mang đến một 'phước lành'. Một bức ảnh không phải là tập hợp pixel ngẫu nhiên, chúng bị ràng buộc bởi hình khối và ánh sáng. Toàn bộ kho tàng hình ảnh tự nhiên, trên thực tế, lại cư ngụ trên những không gian con có số chiều nội tại cực kỳ nhỏ.
Trong ngôn ngữ toán học, ta có thể mô phỏng cấu trúc này bằng một Hỗn hợp Gauss hạng thấp, gọi là MoLRG. Thay vì là một đám mây khối cầu khổng lồ trong không gian $d$ chiều, dữ liệu thực chất tụ tập lại quanh những mặt phẳng mỏng manh $U_i$. Nhiệm vụ của quá trình học không còn là lấp đầy không gian quá rộng, mà là định vị được các mặt phẳng này."


### Scene 5: Phép chiếu Hình học và Sự tương đương với PCA (4:45 - 6:05)
*Mục tiêu: Dùng trực giác của phép chiếu (projection) để giải thích PCA và hiện tượng chuyển pha.*
*Thời lượng: 90 giây (182 từ).*

**[4:45 - 5:10] Manim Visual:** Đưa màn hình về 2D. Viết hàm mục tiêu khử nhiễu quen thuộc: $\min_\theta \mathbb{E} \left[ ||\epsilon - s_\theta(x_t, t)||^2 \right]$. Sử dụng `TransformMatchingTex` biến đổi hàm này qua lăng kính công thức Tweedie, làm nổi bật thông điệp: Việc đoán nhiễu (Score) thực chất là mạng đang cố gắng ước lượng lại ảnh gốc $\mathbb{E}[x_0|x_t]$.

**[5:10 - 5:40] Manim Visual:** Mở ra không gian 3D. Vẽ một mặt phẳng 2D trong suốt (đại diện cho không gian con $U$) và một điểm nhiễu $x_t$ lơ lửng bên trên. Dùng `DashedLine` chiếu vuông góc điểm $x_t$ xuống mặt phẳng để tạo ra điểm $\hat{x}_0$. Hiện công thức chiếu: $\hat{x}_0 = U U^T x_t$. Sau đó dùng `Transform` biến bài toán nơ-ron thành PCA: $\max_U ||UX||_F^2 \quad \text{s.t.} \quad U^T U = I$.

**[5:40 - 6:05] Manim Visual:** Mở ra một `Axes` 2D. Trục hoành là lượng dữ liệu log $\log_2(N/ID)$, trục tung là khả năng khái quát. Dùng `UpdateFromAlphaFunc` vẽ một đường cong nằm ngang sát đáy, đến một ngưỡng (threshold $N > c \cdot ID$) thì vọt thẳng lên cao (Generalization Phase).

**[Voiceover]**
"Vậy mạng nơ-ron học các mặt phẳng này như thế nào? Lời giải nằm ở công thức Tweedie. Công thức này chứng minh rằng: tối ưu hàm đoán nhiễu của quá trình Diffusion... thực chất là ta đang cố gắng ước lượng lại bức ảnh gốc.


Về mặt hình học, nếu dữ liệu cư ngụ trên một mặt phẳng, cách tốt nhất để khử nhiễu là chiếu vuông góc điểm nhiễu đó xuống mặt phẳng. Toán học chỉ ra rằng, mạng nơ-ron lúc này hoạt động chính xác như một phép chiếu tuyến tính với ma trận $UU^T$. Nhờ vậy, hàm loss phức tạp của mạng Deep Learning bỗng chốc thu gọn thành bài toán Phân tích thành phần chính — PCA. Mô hình đang tự xoay ma trận $U$ để bao trọn lấy nhiều dữ liệu nhất có thể.

Sự tương đương này dẫn đến một hiện tượng chuyển pha vật lý ngoạn mục. Lượng ảnh cần để huấn luyện không phụ thuộc vào số pixel, mà tỷ lệ thuận với số chiều nội tại của dữ liệu. Chỉ khi vượt qua ngưỡng này, mô hình mới bừng tỉnh, phá vỡ trạng thái học vẹt để tiến thẳng vào vùng Khái quát hóa."


---

### Scene 6: Quyền năng của Ma trận $U$ – Từ Chỉnh sửa đến Bảo mật (6:05 - 7:20)**
*Mục tiêu: Trình bày ứng dụng của ma trận không gian con (LOCO Edit) và không gian bù (Watermarking).*
*Thời lượng: 90 giây (khoảng 170 từ).*

**[6:05 - 6:30] Manim Visual:** Tái hiện lại mặt phẳng $U$ từ Scene 5. Một bức ảnh khuôn mặt được chiếu lên mặt phẳng này. Dùng `Vector` vẽ các hệ vector cơ sở $u_1, u_2, ...$ xuất phát từ tâm bức ảnh. Khi một vector cơ sở kéo dài ra, các thuộc tính của bức ảnh thay đổi theo (ví dụ: khuôn mặt cười lên, tóc dài ra). Hiện chữ: **"Semantic Steering Vectors"**.

**[6:30 - 6:55] Manim Visual:** Dùng `Brace` để chỉ định phần không gian nằm ngoài mặt phẳng $U$, gọi là **Null Space** (Không gian không). Một mảng thông tin mã hóa (Watermark) được đẩy vào vùng này. Bức ảnh gốc không hề thay đổi về mặt thị giác, nhưng khi quét qua một bộ lọc toán học, thông tin ẩn hiện lên rực rỡ.

**[6:55 - 7:20] Manim Visual:** Hiển thị tên kỹ thuật: **LOCO Edit** và **Shallow Diffuse**. Quay trở lại biểu đồ chuyển pha ở Scene 2, nhấn mạnh rằng chỉ khi mô hình "khái quát hóa" (Generalization), các không gian này mới thực sự ổn định để thao tác.

**[Voiceover]**
"Khi mạng nơ-ron đã tìm ra ma trận $U$, nó không chỉ đơn thuần là giải xong một bài toán. Ma trận này chính là bảng điều khiển tối thượng cho sự sáng tạo.

Mỗi cột trong $U$ đóng vai trò như một 'vector ngữ nghĩa'. Bằng cách di chuyển dọc theo các vector này — một kỹ thuật gọi là LOCO Edit — ta có thể thay đổi các đặc tính cụ thể của bức ảnh như nụ cười, kiểu tóc hay ánh sáng một cách độc lập và chính xác, mà không làm hỏng cấu trúc tổng thể. Đây chính là sự kỳ diệu của việc làm chủ không gian con chiều thấp.

Nhưng quyền năng không chỉ nằm ở những gì mô hình thấy, mà còn ở những gì nó lờ đi. Không gian bù, hay Null Space, là nơi mạng nơ-ron không chứa dữ liệu. Chúng ta có thể tận dụng 'vùng tối' này để giấu các thủy ấn kỹ thuật số. Thủy ấn này hoàn toàn vô hình và bền bỉ, giúp bảo vệ bản quyền hình ảnh mà không gây ra bất kỳ sự biến dạng nào.

Lý thuyết không gian con, vì thế, đã biến quá trình khuếch tán từ một hộp đen ngẫu nhiên thành một công cụ kỹ thuật có độ chính xác tuyệt đối."

---

### Scene 7: Định lượng qua Probability Flow Distance (7:20 - 8:25)
**Mục tiêu:** Giới thiệu PFD làm thước đo.
**Thời lượng:** 90 giây (khoảng 160 từ).

* **[7:20 - 7:40] Manim Visual:** Chia đôi màn hình. Nửa trái: Mô hình Teacher (đại diện $p_{\theta^*}$). Nửa phải: Mô hình Student (đại diện $p_\theta$).
* **[7:40 - 8:05] Manim Visual:** Vẽ 2 quỹ đạo đường cong (ODE trajectory) chạy song song từ cùng một mảng nhiễu $x_T$ về tâm. 
* **[8:05 - 8:25] Manim Visual:** Dùng `MathTex` hiện công thức PFD, đồng thời vẽ các đường `DashedLine` nối sự chênh lệch giữa hai điểm cuối của 2 quỹ đạo.
    $$PFD(p_\theta, p_{\theta^*}) = \mathbb{E}_{x \sim \mathcal{N}(0, T^2I)} \left[ ||\Phi_{p_\theta}(x_T) - \Phi_{p_{\theta^*}}(x_T)||^2 \right]$$

**[Voiceover]**
"Tuy nhiên, làm sao để đo lường định lượng sự khái quát này, khi ta vĩnh viễn không biết được phân phối thực của tự nhiên? 
Giải pháp là thiết lập một hệ quy chiếu: Ta dùng một mô hình Teacher đóng vai trò là chân lý tạo ra dữ liệu, và một mô hình Student học từ lượng dữ liệu đó. 
Thay vì đếm pixel hay dùng các thang đo như FID, ta đo lường khoảng cách giữa các quỹ đạo động lực học thông qua Probability Flow Distance — viết tắt là PFD. Thước đo này tính toán chuẩn bình phương sự sai lệch giữa điểm đích mà quỹ đạo ODE của Student đạt đến, so với quỹ đạo chuẩn xác của Teacher, khi cả hai cùng xuất phát từ một điểm nhiễu $x_T$."

### Scene 8: Động lực học Học tập và Hiện tượng Đổ đèo kép (8:25 - 9:30)
**Mục tiêu:** Đưa ra khái niệm Double Descent.
**Thời lượng:** 90 giây (khoảng 150 từ).

* **[8:25 - 8:45] Manim Visual:** Xóa toàn bộ. Vẽ một `Axes` biểu diễn quá trình huấn luyện. Trục hoành: Số Epochs. Trục tung: Lỗi khái quát hóa (Generalization Error - đo bằng PFD).
* **[8:45 - 9:10] Manim Visual:** Bắt đầu vẽ đường cong huấn luyện. Đường cong đi xuống đều... rồi đột ngột vòng lên tạo thành một đỉnh chóp sắc nhọn... sau đó tiếp tục đổ dốc (Descent) cắm xuống vùng cực tiểu ổn định. 
* **[9:10 - 9:30] Manim Visual:** Dùng các mũi tên chỉ vào chóp nhọn, ghi chú "High Variance" (Màu đỏ) và "Low Bias" (Màu xanh). Hiện cụm từ "Epoch-wise Double Descent". Dừng hình.

**[Voiceover]**
"Khi quan sát sự tiến hóa của khoảng cách PFD xuyên suốt quá trình huấn luyện, ta bắt gặp một hành vi vật lý đầy tính nghịch lý: Hiện tượng đổ đèo kép — Double Descent.
Ở những Epoch đầu tiên, lỗi giảm dần do mô hình cố gắng ghi nhớ dữ liệu. Nhưng sau đó, đường cong đột ngột tăng vọt lên, phá vỡ mọi sự ổn định. Đây là khoảnh khắc mô hình rơi vào cuộc chiến khốc liệt nhất giữa Phương sai và Độ chệch (Bias-Variance Tradeoff) khi phải xấp xỉ một không gian quá lớn.
Nhưng, nếu ta kiên nhẫn huấn luyện xuyên qua 'cơn bão' này, mô hình sẽ tự tái cấu trúc, bước vào lần đổ đèo thứ hai, và hội tụ vĩnh viễn về quỹ đạo hình học chuẩn xác nhất của dữ liệu."


---

## Phần 2: Hình học của sự Khái quát hóa trong Diffusion Models

### Scene 1: Bức tranh toàn cảnh và Bản chất của Hàm Score (09:40 - 11:10)

* **[09:40 - 10:05] Manim Visual:**
Mở đầu bằng phông nền đen. Một bức ảnh chú ngựa sắc nét ($X_0$) xuất hiện ở trung tâm. Chữ "**Forward Process**" hiện lên phía trên. Bức ảnh bắt đầu mờ dần, các hạt nhiễu Gaussian li ti xuất hiện và dày đặc hơn qua các mốc thời gian $X_1, X_2, \dots$ cho đến khi chỉ còn là một khối nhiễu vô định hình $X_T$.

Phía dưới quá trình này, xuất hiện phương trình vi phân ngẫu nhiên (SDE) đại diện cho việc thêm nhiễu:


$$dX_t = \underbrace{-\frac{1}{2}\beta(t)X_t dt}_{\text{Suy giảm (Drift)}} + \underbrace{\sqrt{\beta(t)} dW_t}_{\text{Khuếch tán (Noise)}}$$


Hai cụm từ "**Suy giảm**" và "**Khuếch tán**" được highlight bằng hai màu khác nhau để người xem dễ phân biệt.

**[Audio]**
Xin chào các bạn. Hãy tưởng tượng quá trình sáng tạo của một mô hình AI giống như việc điêu khắc từ một khối đá xù xì. Trong các mô hình Diffusion, chúng ta bắt đầu bằng Quá trình Thuận: tiêm nhiễu dần dần vào dữ liệu gốc cho đến khi mọi cấu trúc biến mất hoàn toàn.

Về mặt toán học, đây là một phương trình vi phân ngẫu nhiên (SDE). Nó gồm hai lực đối nghịch: một lực "suy giảm" kéo dữ liệu về gốc tọa độ, và một lực "khuếch tán" đẩy dữ liệu vào sự hỗn loạn của nhiễu thuần túy.

* **[10:05 - 10:35] Manim Visual:**
Một mũi tên lớn quay ngược lại: "**Reverse Process**". Từ khối nhiễu $Y_T$, các hạt nhiễu bắt đầu được "sắp xếp" lại để hình thành hình dáng chú ngựa $Y_0$.
Ngay tại điểm khuếch tán, một biểu tượng chiếc la bàn hiện ra, bên cạnh là công thức hàm Score:

$$s_t^*(\cdot) := \nabla \log p_{X_t}(\cdot)$$


**[Audio]**
Để đảo ngược quá trình này, ta cần một "chiếc la bàn" để tìm đường quay lại từ hư không. Đó chính là hàm Score Stein. Nó không phải là một con số tĩnh, mà là một trường vector chỉ ra hướng mà mật độ dữ liệu tăng nhanh nhất. Nói cách khác, hàm Score chính là "bản năng nghệ thuật" giúp mô hình biết cần phải gột rửa nhiễu ở đâu để lộ ra cấu trúc dữ liệu ẩn giấu.

* **[10:35 - 11:10] Manim Visual:**
Từ "chiếc la bàn" này, màn hình tách ra làm hai quỹ đạo chạy song song:

1. **Nhánh 1 (Lấy mẫu ngẫu nhiên - DDPM):** Các điểm dữ liệu di chuyển có chút rung động (stochastic).

$$dY_t = [Y_t + 2s_{T-t}^*(Y_t)]\beta dt + \sqrt{2\beta}dW_t$$

2. **Nhánh 2 (Quỹ đạo tất định - DDIM):** Các điểm di chuyển mượt mà thành một đường cong duy nhất (deterministic).

$$dY_t = [Y_t + s_{T-t}^*(Y_t)]\beta dt$$

**[Audio]**
Men theo chiếc la bàn này, chúng ta có hai lộ trình chính. Lộ trình thứ nhất là DDPM – một quá trình ngẫu nhiên, nơi mỗi bước đi đều có sự xáo trộn nhẹ để tìm kiếm sự đa dạng. Lộ trình thứ hai thanh lịch hơn, gọi là Probability Flow ODE, đại diện cho phương pháp DDIM tất định. Ở đây, mỗi điểm nhiễu ban đầu sẽ đi theo một quỹ đạo duy nhất và chính xác để trở thành dữ liệu. Cả hai con đường đều dựa trên giả định rằng chúng ta đã sở hữu một hàm Score hoàn hảo.


---

### Scene 2: Hố sâu giữa Lý thuyết và Thực hành (11:10 - 12:00)

* **[11:10 - 11:35] Manim Visual:**
Chuyển cảnh. Màn hình hiện lên một cán cân. Một bên là biểu tượng "Lý thuyết" với đồ thị hàm $O(d/\epsilon)$. Bức ảnh minh họa ImageNet xuất hiện với con số $d = 150,528$ pixels. Bên kia là "Thực hành" với một thanh tiến trình chạy từ 1 đến 100 steps.

**[Audio]**
Nếu chúng ta có một hàm Score hoàn hảo, việc lấy mẫu sẽ dễ dàng. Nhưng trong thực tế, không gian dữ liệu thường cực kỳ khổng lồ. Hãy lấy ImageNet làm ví dụ, mỗi bức ảnh có số chiều $d$ lên tới hơn 150,000.

* **[11:35 - 12:00] Manim Visual:**
Đưa ra công thức đánh giá giới hạn hội tụ Total Variation (TV). Dòng text nổi bật: "Iteration complexity: $d/\epsilon$". Màn hình tính toán nhanh $\frac{150528}{\epsilon}$ và cho ra kết quả $> 10^6$. Chữ "$10^6$ steps" nhấp nháy màu đỏ.

**[Audio]**
Các giới hạn lý thuyết cổ điển cho cả DDPM và DDIM chỉ ra rằng, để đạt được độ sai số (Total Variation) nhỏ hơn $\epsilon$, số bước lặp cần thiết tỉ lệ thuận với số chiều không gian $d$, tức là cỡ $\tilde{O}(d/\epsilon)$. Với ImageNet, điều này đồng nghĩa với việc ta cần hàng triệu bước lấy mẫu! Thế nhưng, hãy nhìn vào thực tế. Các mô hình DDPM hay DDIM hoạt động cực tốt chỉ với hàng trăm, thậm chí vài chục bước. Tại sao lại có sự chênh lệch đáng kinh ngạc này? Mô hình đang giấu chúng ta điều bí mật gì?


---

### Scene 3: Sự tự do của Dữ liệu thực và Lời giải từ Chiều nội tại (12:00 - 14:20)

* **[12:00 - 12:45] Manim Visual:**
Màn hình đang hiển thị câu hỏi từ Scene 2: *"Mô hình đang giấu chúng ta điều bí mật gì?"*
Ngay sau đó, một biểu đồ hình chuông (Bell curve) hoàn hảo, trơn lấp lánh xuất hiện. Bên cạnh là các dòng chữ mờ nhạt: *Log-concavity, Smoothness*. Đột nhiên, biểu đồ hình chuông vỡ vụn thành hàng triệu điểm sáng li ti, bay lộn xộn trong một không gian 3D tối.
Một quả cầu ánh sáng mờ ảo xuất hiện, bao bọc toàn bộ hàng triệu điểm sáng đó lại. Ở góc màn hình hiện lên một điều kiện toán học duy nhất:


$$\mathbb{P}(||X_0||_2 \le T^{c_R}) = 1$$

**[Audio]**
Bí mật đầu tiên nằm ở cách chúng ta nhìn nhận dữ liệu. Trong nhiều năm, để chứng minh một mô hình hội tụ, các nhà toán học thường ép dữ liệu phải tuân theo những giả định rất "đẹp" nhưng phi thực tế như tính trơn (smoothness) hay lồi logarit (log-concavity).
Nhưng hình ảnh thực tế thì không hoàn hảo như vậy. Chúng hỗn loạn và cực kỳ phức tạp. Bước đột phá của lý thuyết hội tụ hiện đại là nó hoàn toàn rũ bỏ những ràng buộc gò bó này. Mô hình Diffusion không quan tâm không gian hỗ trợ (support size) của dữ liệu lớn đến mức nào. Nó chỉ cần một điều kiện tiên quyết duy nhất: Dữ liệu được giới hạn trong một quả cầu không gian có bán kính đủ lớn (polynomially large diameter). Sự giải phóng này đưa toán học chạm mặt trực tiếp với thực tiễn.

* **[12:45 - 13:25] Manim Visual:**
Camera zoom xuyên qua lớp vỏ quả cầu ánh sáng, tiến sâu vào đám mây điểm dữ liệu hỗn loạn. Khi camera xoay một góc 90 độ, một góc nhìn mới lộ ra: hàng triệu điểm sáng tưởng chừng lộn xộn ấy thực chất lại bám chặt lấy một dải ruy băng 2D mỏng lượn sóng (Manifold) uốn lượn trong không gian 3D.
Dòng chữ nhấp nháy chỉ vào dải ruy băng: *Intrinsic dimension $k \approx 43$* (bên dưới là *ImageNet $d \approx 150K$*).

**[Audio]**
Và khi ta được phép nhìn vào hình dáng thật của dữ liệu thực, bí mật thứ hai – cũng là bí mật lớn nhất – xuất hiện. Mặc dù hình ảnh tồn tại trong không gian hàng trăm ngàn chiều, nhưng cấu trúc thực sự tạo nên chúng lại nằm trên một đa tạp (manifold) uốn lượn có số chiều thấp hơn rất rất nhiều. Khái niệm này gọi là chiều nội tại, hay $k$. Đối với một tập dữ liệu đồ sộ như ImageNet, $k$ thực chất chỉ rơi vào khoảng 43.

* **[13:25 - 14:20] Manim Visual:**
Định lý hiện ra tỏa sáng: **Theorem (Liang, Huang, Chen '24)**. Cụm từ *Iteration complexity: $\tilde{O}(k/\epsilon)$* được làm nổi bật.
Để giải thích, công thức Tweedie hiện ra, từ từ thay thế thành phần drift trong SDE:

$$dY_t = (c_{1,t}Y_t + c_{2,t}\mathbb{E}[X_0|X_{T-t}=Y_t])dt + \sqrt{2}dB_t$$



Cụm kỳ vọng có điều kiện $\mathbb{E}[X_0|X_t]$ được highlight màu vàng. Hình ảnh một điểm bị nhiễu văng ra khỏi dải ruy băng lập tức bị một lực vô hình chiếu thẳng góc, kéo giật trở lại bám sát vào bề mặt ruy băng. Chữ "Projection" xuất hiện bên cạnh cụm kỳ vọng.

**[Audio]**
Toán học cuối cùng đã bắt kịp thực nghiệm! Các chứng minh mới nhất cho thấy, cả DDPM và DDIM tự động thích ứng một cách kỳ diệu với cấu trúc chiều thấp này. Số bước thực tế cần thiết không bị trói buộc bởi số chiều $d$ khổng lồ nữa, mà chỉ phụ thuộc vào chiều nội tại $k$.
Cơ chế đằng sau sự màu nhiệm này được lý giải qua công thức Tweedie. Thành phần kỳ vọng $\mathbb{E}[X_0|X_t]$ không đơn thuần chỉ là một biến số. Nó hoạt động như một phép "chiếu" không gian. Dù quá trình nhiễu loạn khuếch tán dữ liệu ra mọi hướng trong không gian khổng lồ, phép chiếu này liên tục như một sợi dây thun, kéo các điểm dữ liệu quay trở lại và bám sát vào cấu trúc đa tạp chiều thấp.

---

### Scene 4: Xấp xỉ bậc cao - Bứt tốc bằng Giải tích số (14:20 - 17:40)

* **[14:20 - 15:00] Manim Visual:** Màn hình xuất hiện hình ảnh một chú rùa đang bò chậm chạp, cõng trên lưng dòng chữ *"100s - 1000s steps"*. Một tia chớp xẹt qua đánh tan chú rùa, để lại dòng chữ rực sáng: **"Training-free Acceleration"** (Tăng tốc không cần huấn luyện).
Camera chuyển dời tới một trục thời gian của ODE, di chuyển lùi từ mốc $t$ về $t-1$. Màn hình hiện lên công thức tích phân cốt lõi để bước từ $Y_t$ sang $Y_{t-1}$:



$$Y_{\overline{\alpha}_{t-1}}^{ode} = \frac{1}{\sqrt{\alpha_t}} Y_{\overline{\alpha}_t}^{ode} + \int_{\overline{\alpha}_t}^{\overline{\alpha}_{t-1}} \frac{1}{\sqrt{\gamma^3}} s_\gamma^*(Y_\gamma^{ode}) d\gamma$$



**[Audio]**
Dù mô hình đã khéo léo lách qua khe cửa hẹp của chiều nội tại, việc phải bò từng chút một qua hàng trăm bước lặp vẫn là một rào cản tính toán khổng lồ. Câu hỏi đặt ra là: Liệu ta có thể tạo ra một bộ lấy mẫu nhanh hơn bằng toán học thuần túy, mà không tốn một xu để huấn luyện lại mô hình?
Bản chất của việc lấy mẫu thực ra là giải một phương trình vi phân. Cụ thể hơn, là làm sao để tính được chính xác cái tích phân cốt lõi này.

* **[15:00 - 15:45] Manim Visual:** Thành phần hàm Score $s_\gamma^*(Y_\gamma^{ode})$ bên trong tích phân được bôi sáng. Đồ thị hàm Score hiện ra là một đường cong uốn lượn. Dòng chữ **"1st order approx (DDIM)"** xuất hiện. Để xấp xỉ diện tích dưới đường cong, một hình chữ nhật thô kệch, nằm ngang vắt ngang qua khoảng thời gian, với công thức $s_\gamma^*(Y_\gamma^{ode}) \approx s_t(Y_t)$.



**[Audio]**
Phương pháp DDIM truyền thống mà chúng ta vẫn dùng thực chất chỉ là một phép xấp xỉ bậc 1. Nó ngây thơ giả định rằng "chiếc la bàn" hàm Score gần như đứng yên, không thay đổi hướng trong suốt một bước thời gian ngắn. Giống như bạn đang cố gắng tính diện tích dưới một đường cong mềm mại bằng cách dùng các hình chữ nhật thô kệch vậy.

* **[15:45 - 16:30] Manim Visual:** Hình chữ nhật vụn vỡ. Dòng chữ **"K-th order approx (Lagrange Interpolation)"** hiện ra. Thay vì một đường nằm ngang, $K$ chấm sáng (điểm neo - anchor points) xuất hiện rải rác dọc theo đường cong thực tế. Một đường cong đa thức (polynomial) cực kỳ mượt mà tự động vẽ vắt qua $K$ điểm này, khớp gần như hoàn hảo với đường cong gốc của hàm Score.



**[Audio]**
Nhưng toán học giải tích cho ta công cụ sắc bén hơn nhiều. Thay vì đoán mò bằng đường thẳng, tại sao ta không xấp xỉ quỹ đạo của hàm Score bằng đa thức nội suy Lagrange?
Chúng ta chỉ cần chọn ra $K$ điểm neo trên quỹ đạo, và vẽ một đường cong đa thức mượt mà đi qua chúng để dự đoán chính xác sự uốn lượn của chiếc la bàn. Bằng cách liên tục tinh chỉnh các điểm neo này, ta xấp xỉ tích phân với độ chính xác cao hơn hẳn.

* **[16:30 - 16:50] Manim Visual:** Định lý cuối cùng xuất hiện hoành tráng trên màn hình: **Theorem (Li, Zhou, Wei, Chen '25)**. Cụm từ "Iteration Complexity:" thay đổi từ $(d/\epsilon)$ rớt mạnh xuống còn $\tilde{O}(d^{1+2/K} / \epsilon^{1/K})$. Một biểu đồ so sánh nhanh hiện ra: Đường cong của $(d/\epsilon)$ dốc đứng khi độ lỗi $\epsilon$ nhỏ đi, trong khi đường của $(d^{1+2/K} / \epsilon^{1/K})$ làu làu, nằm là đà dưới thấp (thể hiện thời gian chạy cực ngắn).



**[Audio]**
Kết quả của phép nội suy này thật sự kinh ngạc! Định lý mới nhất chứng minh rằng, với bộ lấy mẫu bậc $K$, số bước lặp không còn tỉ lệ thuận với $(1/\epsilon)$ nữa, mà giảm mạnh xuống chỉ còn $(1/\epsilon)^{1/K}$. Dù nó phải đánh đổi bằng việc chịu ảnh hưởng một chút từ số chiều không gian $d$, nhưng hãy thử tưởng tượng: khi yêu cầu về độ sắc nét của bức ảnh càng cao (tức là độ lỗi $\epsilon$ cực kỳ nhỏ), phương pháp bậc $K$ này sẽ bứt tốc ngoạn mục, bỏ xa các phương pháp truyền thống. Vẻ đẹp của toán học đã một lần nữa giải cứu chúng ta, mang đến một thuật toán tăng tốc đầy thanh lịch mà không đòi hỏi bất kỳ sự can thiệp nào vào trọng số của mô hình!

* **[16:50 - 17:15] Manim Visual:** Đồ thị từ từ thu nhỏ lại nhường chỗ cho một không gian thử nghiệm. Màn hình được chia làm hai nửa rõ rệt để chuẩn bị cho một cuộc đua trực quan: Bên trái (1st Order - DDIM) xuất hiện một khối nhiễu hạt Gaussian, kèm theo biểu tượng chú rùa và bộ đếm *Step: 0 / 1000*. Bên phải (K-th Order Approx) một khối nhiễu tương tự, kèm theo biểu tượng tia chớp và bộ đếm *Step: 0 / 20*.
Cuộc đua bắt đầu! Bên trái nhích từng bước ngắn, thay đổi rất chậm chạp. Bên phải nhảy những bước lớn, khối nhiễu biến đổi một cách đột phá và chỉ sau vài chục bước lặp, một chú ngựa sắc nét hoàn hảo đã xuất hiện tự hào trên màn hình. Dòng chữ lớn hiện ra vắt ngang màn hình: **"Provable Training-Free Acceleration"**.



**[Audio]**
Những giới hạn lý thuyết này nghe có vẻ trừu tượng, nhưng để thực sự cảm nhận được sức mạnh của giải tích số, hãy cùng xem một cuộc đua thực tế. Chúng ta sẽ cùng giải mã một khối nhiễu để tìm lại hình ảnh chú ngựa ban đầu. Bên trái, bộ lấy mẫu bậc 1 truyền thống đang chật vật dò dẫm từng bước ngắn qua hàng ngàn vòng lặp. Trong khi đó, bên phải, nhờ khả năng nội suy đường cong của hàm Score, thuật toán bậc $K$ có thể thực hiện những bước nhảy vọt cực dài mà không sợ bị chệch hướng. Kết quả là chú ngựa sắc nét hiện ra chỉ trong một phần nhỏ thời gian, minh chứng hoàn hảo cho việc tăng tốc không cần huấn luyện lại.

* **[17:15 - 17:40] Manim Visual:** Hai nửa màn hình hòa lại làm một. Bức ảnh chú ngựa hoàn thiện từ phương pháp bậc $K$ nằm ở trung tâm. Sau đó, bức ảnh thu nhỏ lại và hóa thành một điểm sáng, di chuyển trên một "cây cầu" bắc qua một khe nứt lớn. Phía bên kia bờ là những khối hình học lơ lửng mang theo các dấu chấm hỏi. Các dòng chữ lần lượt xuất hiện dưới dạng các nhánh rẽ: *End-to-end theory?* , *High-order stochastic samplers?* , *Discrete-valued problems?*.


**[Audio]**
Sự thanh lịch của toán học đã giúp chúng ta bứt tốc các thuật toán nặng nề nhất. Tuy nhiên, bức tranh về Diffusion vẫn chưa hoàn thiện. Giải tích số đã giải quyết tốt phần lấy mẫu, nhưng điều gì sẽ xảy ra nếu ta gộp chung cả sai số trong quá trình huấn luyện hàm Score để tạo thành một lý thuyết toàn vẹn (end-to-end theory)? Hay làm thế nào để xây dựng các bộ lấy mẫu ngẫu nhiên (stochastic) bậc cao? Xa hơn nữa, liệu những phép chiếu này có thể áp dụng cho các không gian dữ liệu rời rạc (discrete-valued) như văn bản chữ viết thay vì hình ảnh liên tục? Đây chính là những bài toán mở đầy hấp dẫn đang chờ đợi phía trước...

---

## Phần 3: Diffusion Inverse Solvers for Scientific Applications


### Scene 1: Bản chất của Bài toán Ngược (17:50 - 18:55)

**Trọng tâm:** Định hình "Inverse Problem" qua lăng kính của nhiễu và toán tử thuận.

* **[17:50 - 18:05] Manim Visual:** * Mở đầu bằng một lưới điểm ảnh đen trắng mờ ảo, sau đó `FadeIn` một bộ não người (ảnh chụp MRI chất lượng cao). Đặt tên là biến $x$. Tạo một mũi tên chuyển đổi `Arrow()`, gắn nhãn $\mathcal{A}(\cdot)$ (Toán tử thuận - Forward Operator)
* **[18:05 - 18:35] Manim Visual:** Biến bức ảnh sắc nét thành các đường cong tín hiệu rời rạc, thưa thớt. Thêm một vector nhiễu ngẫu nhiên nhỏ (Gaussian noise) rơi vào các đường cong này. `Write()` công thức trung tâm: $y = \mathcal{A}(x) + n$.
* **[18:35 - 18:55] Manim Visual:** Dùng `Transform()` để đảo ngược mũi tên từ $y$ về $x$, đặt dấu chấm hỏi lớn, biểu diễn "Inverse Problem".


* **Audio (Narration):**
"Trong y tế, hay rộng hơn là các ứng dụng khoa học, chúng ta hiếm khi quan sát trực tiếp được chân lý. Những gì một máy chụp MRI hay CT nhận được không phải là hình ảnh nguyên bản, mà là các tín hiệu đo lường rời rạc, thường là không đầy đủ và lẫn nhiễu.
Nếu ta gọi hình ảnh thực tế mà ta muốn tìm là $x$, thì quá trình thu thập dữ liệu có thể được mô tả bằng một phương trình đơn giản: $y = \mathcal{A}(x) + n$.
Trong đó, $y$ là những gì ta quan sát được, $\mathcal{A}$ là toán tử thuận – đại diện cho hệ thống vật lý của máy đo, và $n$ là nhiễu không thể tránh khỏi. Bài toán đặt ra là: Làm sao để đi ngược từ $y$ về $x$? Lời giải trực tiếp thường vô vọng, bởi đây là một bài toán 'ill-posed' – có vô số bức ảnh $x$ có thể tạo ra cùng một kết quả đo $y$."

---

### Scene 2: Góc nhìn Bayes và Dòng chảy Khuếch tán (18:55 - 20:25)

**Mục tiêu:** Giải thích định lý Bayes bằng Vector Field và trực giác về lực kéo của dữ liệu qua phương pháp DPS.
**Thời lượng:** 90 giây (Khoảng 185 từ).

* **[18:55 - 19:20] Manim Visual:** Vẽ một không gian 2D với các cụm điểm dữ liệu mờ ảo (data manifold). Sử dụng `VectorField()` để tạo các mũi tên nhỏ, mờ hướng về vùng có mật độ điểm cao nhất. Xuất hiện công thức Bayes trung tâm: $\nabla_{x}\log p(x|y) = \nabla_{x}\log p(x) + \nabla_{x}\log p(y|x)$.
* **[19:20 - 19:50] Manim Visual:** Khi Voiceover nhắc đến "Tiền nghiệm", cụm $\nabla_{x}\log p(x)$ sáng lên màu xanh nước biển. Khi nhắc đến "Sự nhất quán", cụm $\nabla_{x}\log p(y|x)$ sáng lên màu vàng rực. Diễn hoạt một điểm nhiễu $x_t$ đang lơ lửng bị hai mũi tên (xanh và vàng) cùng tác động lực.
* **[19:50 - 20:25] Manim Visual:** Chuyển cảnh nhịp nhàng, viết công thức xấp xỉ DPS: $\text{Gradient} \approx \nabla_{x_t} ||y - \mathcal{A}(\hat{x}_0)||^2$. Zoom nhẹ vào cụm sai số.



**[Audio (Narration)]**
"Để giải quyết sự mơ hồ của bài toán ngược, chúng ta cần một sự kết hợp giữa 'kinh nghiệm' và 'bằng chứng'. Đây chính là nơi định lý Bayes thể hiện quyền năng của mình.

Hãy tưởng tượng quá trình này như một cuộc giằng co giữa hai lực lượng. Thành phần màu xanh này là 'Tiền nghiệm' (Prior) – nó đóng vai trò như một chiếc la bàn nội tại mà mô hình Diffusion đã học được. Chiếc la bàn này luôn chỉ hướng để đẩy những điểm nhiễu vô nghĩa về phía hình dáng của một bức ảnh thực tế.

Nhưng bấy nhiêu là chưa đủ, chúng ta còn cần thành phần màu vàng – 'Sự nhất quán với dữ liệu' (Data Consistency). Đây giống như một thanh nam châm mạnh mẽ, liên tục kéo bức ảnh về phía khớp với những gì máy đo đã ghi lại.

Thách thức nằm ở chỗ: làm sao để tính toán lực kéo này khi bức ảnh vẫn còn đầy nhiễu? Phương pháp DPS giải quyết điều này bằng một trực giác đơn giản: Tại mỗi bước, mô hình sẽ 'nhìn nhanh' về kết quả dự đoán cuối cùng, so sánh nó với dữ liệu thực tế $y$ để tìm ra sai số. Chính đạo hàm của sai số này tạo ra lực nắn chỉnh, đảm bảo bức ảnh không chỉ đẹp, mà còn phải đúng với sự thật vật lý."


---

### Scene 3: Không gian Ẩn và Điểm mù Phi tuyến (20:25 - 21:55)

*Trọng tâm: Trực quan hóa Latent Space và cách thuật toán Resampling vượt qua rào cản của hàm phi tuyến mà không cần tính đạo hàm phức tạp.*

**[20:25 - 20:50] Manim Visual:**
* Màn hình hiện lên một khối lập phương lưới khổng lồ đang xoay chậm, đại diện cho dữ liệu y tế CT/MRI 3D ($512^3$). Biểu tượng thanh RAM bên cạnh đỏ rực và rung lên (báo hiệu quá tải).
* Dùng hàm `Transform()`, nén khối lập phương khổng lồ đi qua một mặt phẳng phát sáng (Encoder $\mathcal{E}$) để biến thành một khối nhỏ gọn hơn rất nhiều. Đặt tên là **Không gian Ẩn (Latent Space)** $z$.

**[20:50 - 21:20] Manim Visual:** 
* Một hạt sáng (đại diện cho quá trình lấy mẫu) di chuyển trơn tru trong không gian $z$.
* Tuy nhiên, khi hạt sáng này chiếu tia (Decoder $\mathcal{D}$) ra ngoài không gian thực để đối chiếu với $y$, tia sáng bị bẻ cong gập khúc nhiều lần. Chữ **"Non-linear Decoder"** hiện lên báo lỗi đứt gãy gradient.

**[21:20 - 21:55] Manim Visual:**
* Xóa đường cong đứt gãy, mũi tên thẳng trực tiếp xuất hiện nối trạng thái hiện tại $z_t'$ và dữ liệu cập nhật $\hat{z}_0(y)$. Khung cảnh mờ đi một chút, hạt sáng "nhảy" sang vị trí mới thông qua một vòng tròn xác suất.
* Ký hiệu công thức trung tâm mượt mà hiện ra:

$$z_t = \text{StochasticResample}(\hat{z}_0(y), z_t')$$


* Ở góc màn hình, chia 2 block nhỏ xuất hiện nhanh: **PaDIS** (xử lý theo mảng) và **Diffusion Blend** (nội suy 3D).

**[Audio (Narration)]**
"Ở bước trước, ta thấy lực kéo nắn chỉnh bức ảnh hoạt động rất hoàn hảo. Tuy nhiên, việc tính toán lực kéo này trực tiếp trên hàng triệu voxel của một khối dữ liệu y tế 3D khổng lồ là một bài toán bất khả thi về mặt phần cứng. Bộ nhớ của hệ thống sẽ nhanh chóng cạn kiệt.

Một giải pháp tự nhiên là dùng một bộ Mã hóa (Encoder) để nén toàn bộ dữ liệu xuống một 'Không gian ẩn' gọn nhẹ hơn rất nhiều. Nhưng cái giá phải trả cho sự gọn nhẹ này là rào cản của sự phi tuyến. Các bộ Giải mã (Decoder) làm nhiệm vụ bung dữ liệu từ không gian ẩn ra ảnh thực giống như những lăng kính cong; chúng bẻ gãy hoàn toàn đường dẫn toán học mà ta dùng để tính toán ngược sai số.

Để vượt qua 'điểm mù' này, thuật toán Lấy mẫu lại ngẫu nhiên (Stochastic Resampling) ra đời. Thay vì cố gắng tính toán đạo hàm một cách vô vọng xuyên qua một hộp đen phi tuyến, thuật toán thực hiện một bước đi khôn ngoan hơn. Nó không tính lực kéo nữa, mà kết hợp trực tiếp tọa độ hiện tại với dữ liệu thực tế để 'bốc thăm' ra một điểm đến hoàn toàn mới.

Giống như việc bạn đang di chuyển trong sương mù và liên tục được dịch chuyển tức thời về đúng đường dựa trên định vị vệ tinh, cơ chế này đảm bảo quỹ đạo sinh ảnh luôn bám chặt lấy thực tế đo lường. Kết hợp cùng các thủ thuật chia nhỏ như PaDIS, ta có thể dễ dàng tái tạo lại những cấu trúc 3D siêu việt mà không sợ hệ thống bị quá tải."

---

### Scene 4: Phá vỡ rào cản thời gian - Từ nghìn bước xuống một bước (21:55 - 23:10)

*Trọng tâm: Giải quyết sự chậm trễ của Diffusion truyền thống bằng Consistency Models (CoSIGN).*

**[21:55 - 22:20] Manim Visual:**

* Màn hình hiện lên một trục thời gian dài với hàng nghìn vạch chia nhỏ, đại diện cho 1000 bước NFEs (Number of Function Evaluations). Một thanh tiến trình chạy chậm chạp, đi kèm biểu tượng đồng hồ cát.

**[22:20 - 22:45] Manim Visual:**
* Xuất hiện một đường cong uốn lượn (quỹ đạo giải ODE). Dùng `Create()` để vẽ một mũi tên nhảy vọt (Skip) từ một điểm bất kỳ $x_t$ trên đường cong thẳng tiến về $x_0$.
* Viết chữ lớn: **Consistency Models**.
* Transform công thức từ Scene 2 thành công thức **CoSIGN**:

$$f(x_t, t) \approx x_0$$

**[22:45 - 23:10] Manim Visual:** 
* Hiệu ứng: Trục thời gian 1000 bước co lại chỉ còn 1 hoặc 2 vạch sáng rực rỡ. Gắn nhãn: **"Real-time Inference"**.

**[Audio (Narration)]**
"Dù đã tối ưu về không gian, Diffusion vẫn vấp phải một rào cản vật lý: Thời gian. Việc phải lặp lại hàng trăm bước tính toán để khử nhiễu là một xa xỉ phẩm mà các bác sĩ trong phòng cấp cứu không thể chờ đợi.
Làm sao để chúng ta có thể 'nhảy cóc' mà không làm mất đi độ chính xác?
Câu trả lời nằm ở mô hình nhất quán – Consistency Models. Thay vì học cách đi từng bước nhỏ trên quỹ đạo giải phương trình vi phân, mô hình giờ đây học cách 'nhìn thấu' tương lai. Nó học một hàm số có khả năng ánh xạ trực tiếp bất kỳ điểm nào trên dòng chảy nhiễu về thẳng điểm gốc dữ liệu sạch.
Với thuật toán CoSIGN, chúng ta kết hợp sức mạnh của tính nhất quán này vào bài toán ngược khoa học. Kết quả là một sự đột phá về hiệu suất: thay vì hàng ngàn bước, giờ đây ta có thể tái tạo hình ảnh y tế sắc nét chỉ trong 1 đến 2 lần chạy mô hình, mở ra cánh cửa cho việc chẩn đoán tức thời ngay tại thời điểm quét."


---


### Scene 5: Chấp nhận Sự thật Ngoài miền - OOD (23:10 - 24:10)

**Trọng tâm:** Tính tổng quát hóa (Generalizability).

**[23:10 - 23:35] Manim Visual:** 
* Vẽ hai đường cong hình chuông (Gaussian distributions) lệch nhau. Nhãn: "Training Distribution" và "Real-world (OOD)".
* Một điểm dữ liệu rơi vào vùng hẹp giữa 2 chuông.

 **[23:35 - 24:10] Manim Visual:**
* Biểu diễn một mạng Neural Network tĩnh. Sau đó, nó bắt đầu nhấp nháy, các trọng số $\theta$ được cập nhật nhẹ (Run-time domain adaptation) dựa trên một điểm dữ liệu hỏng.

**Audio (Narration):**
"Tuy nhiên, thế giới thực không hề lý tưởng. Dữ liệu thực tế thường nằm ngoài phân phối mà mô hình đã được huấn luyện – hay còn gọi là dữ liệu OOD (Out-of-Distribution). Một máy MRI của hãng khác, hoặc một mức độ nhiễu khác hoàn toàn có thể đánh lừa hàm điểm của chúng ta.
Thay vì huấn luyện lại toàn bộ mô hình khổng lồ, ta áp dụng cơ chế thích ứng miền ngay tại thời gian chạy. Thông qua phương pháp Steerable Conditional Diffusion, mô hình tự động điều chỉnh chính nó ngay tại bước lấy mẫu (sampling), chỉ cần dựa trên một dữ liệu đo lường bị hỏng duy nhất bằng một hàm suy hao tự giám sát. Nó giống như việc một cung thủ tự hiệu chỉnh lại kính ngắm ngay trước khi thả dây cung vậy."

---

### Scene 6: Kiểm soát Sự Bất định bằng Toán học (24:10 - 25:50)

*Trọng tâm: Chuyển hóa sự ngẫu nhiên của Diffusion thành sự bất định có kiểm soát phục vụ cho khoa học (Controllability & CCS).*

**[24:10 - 24:35] Manim Visual:** 

* Màn hình chuyển sang một không gian tối, ở giữa là một mặt cầu phát sáng mờ, đại diện cho "Không gian nhiễu ban đầu" (Initial Noise Space).
* Một điểm sáng nằm trên mặt cầu được đánh dấu là $x_T$ (Gốc nhiễu). Từ điểm này, một đường cong sinh ra bức ảnh mục tiêu $x_0$ sắc nét (ví dụ: ảnh một khối u).
* **Hiệu ứng:** Vẽ một vòng tròn nhỏ bao quanh $x_T$, biểu diễn một sự xê dịch (perturbation) nhỏ $\Delta x$.

**[24:35 - 25:10] Manim Visual:**
* Viết công thức xấp xỉ tuyến tính trên góc màn hình (như một "Theoretical Finding"):

$$x_{0}(x_{T}+\lambda\Delta x,T) - x_{0}(x_{T},T) \approx \lambda||\gamma_{0}(x_{T})||$$


* Dùng `Transform()`, khi vector trên mặt cầu nhiễu "xoay" một góc rất nhỏ $\theta$ trong vòng tròn, thì ở đầu kia của đường cong, bức ảnh $x_0$ cũng biến đổi nhẹ nhàng thành các phiên bản $x'_0$ khác nhau (các phương án cấu trúc khối u khác nhau).

**[25:10 - 25:50] Manim Visual:** 
* Viết công thức kỳ vọng hoành tráng ở giữa màn hình:

$$\mathbb{E}[x_{0}^{\prime}] = x_{0} + AE[\Delta x]$$


* Hàng loạt các phiên bản ảnh $x'_0$ được sinh ra, xoay quanh bản gốc $x_0$, tạo thành một "chùm" giải pháp vững chắc.

**[Audio (Narration)]**
"Dù mô hình của chúng ta đã trở nên cực kỳ nhanh chóng và có khả năng thích ứng với mọi loại dữ liệu, nhưng trong khoa học y sinh, có một quy tắc tối thượng: Chúng ta không bao giờ trao phó sinh mạng cho một sự 'ngẫu nhiên vô định'. Khi đối mặt với một dữ liệu không đầy đủ, ta cần một sự đa dạng, nhưng đó phải là một sự đa dạng được kiểm soát chặt chẽ quanh một giới hạn vật lý.

Toán học một lần nữa hé lộ cho chúng ta một đặc tính tuyệt đẹp. Ở bước nhiễu sâu nhất, không gian hoạt động như một hệ thống tuyến tính hoàn hảo. Một dịch chuyển nhỏ, có định hướng trong vùng nhiễu ban đầu sẽ tạo ra một sự thay đổi tỷ lệ thuận tương ứng trên bức ảnh kết quả cuối cùng.

Tận dụng điều này, thuật toán Lấy mẫu Ràng buộc (CCS) ra đời. Nó hoạt động giống như việc thả một mỏ neo. Đầu tiên, mô hình 'đi ngược thời gian' từ một ảnh mục tiêu $x_0$ dự đoán để tìm ra gốc nhiễu tĩnh $x_T$. Sau đó, thay vì lấy một vùng nhiễu ngẫu nhiên hoàn toàn mới để sinh ảnh, thuật toán chỉ khéo léo 'xoay' vector gốc này một góc cực nhỏ.

Kết quả là gì? Ta sinh ra được vô số các biến thể hình ảnh khác nhau, mô tả trọn vẹn những khả năng có thể xảy ra của một căn bệnh. Nhưng điều kỳ diệu nhất là, kỳ vọng toán học của tất cả những biến thể này luôn bị trói buộc chặt chẽ vào cái lõi khoa học ban đầu mà ta đã thả neo. Chúng ta cuối cùng đã thuần phục được sự hỗn mang của Diffusion, biến nó thành một công cụ định lượng đáng tin cậy."

---

## Outro

**Trọng tâm:** Tổng kết triết lý của bài toán và lời chào kết.
**Thời lượng:** Khoảng 45 giây.

**Visual (Manim):** 
* Thu nhỏ đa tạp hình cầu và các phương trình ở scene trước lại.
* `FadeOut` từ từ tất cả các khối hình phức tạp, chỉ giữ lại phương trình cốt lõi ban đầu ở trung tâm màn hình: $y = \mathcal{A}(x) + n$.
* Phương trình này sau đó phát sáng nhẹ rồi mờ dần (`FadeOut`), nhường chỗ cho dòng text: **Harnessing Low Dimensionality in Diffusion
Models: From Theory to Practice - ICML 2026**.


**Audio (Narration):**
"Hành trình mà chúng ta vừa đi qua — từ việc dùng định lý Bayes để dò dẫm trong bóng tối của không gian nhiễu, bẻ cong không gian ẩn để tiết kiệm tài nguyên, cho đến việc dùng hình học thuần túy để trói buộc sự ngẫu nhiên... tất cả đều minh chứng cho một điều.
Sức mạnh thực sự của AI sinh tạo trong khoa học không chỉ nằm ở khả năng khớp dữ liệu khổng lồ, mà nằm ở cách chúng ta dùng toán học để thấu hiểu và kiểm soát cấu trúc của thế giới vật lý.
Nếu bạn muốn tự mình đào sâu hơn vào các chứng minh học thuật này, tôi có để liên kết đến bài diễn thuyết gốc của hội nghị ICML ở phần mô tả.
Và như thường lệ, cảm ơn các bạn đã dành thời gian theo dõi."