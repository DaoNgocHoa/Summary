import nltk

nltk.download('stopwords')
from summarizer import Summarizer

def Return_summary():

    # Tải danh sách từ ngừng tiếng Việt từ một URL
    stopwords_file_path = "E:/pythonProject/Summary/Stopwords.txt"
    file_path = "E:/pythonProject/Directory/J.txt"

    # Đọc tệp từ điển stop words và tạo danh sách
    with open(stopwords_file_path, 'r', encoding='utf-8') as file:
        stopwords_vi = [line.strip() for line in file]

    # Mở tệp văn bản .txt trong chế độ đọc (read)
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            # Đọc nội dung của tệp và lưu vào biến content
            content = file.read()
            # In nội dung ra màn hình
            print("Nội dung tệp văn bản:")

    except FileNotFoundError:
        print(f"Tệp {file_path} không tồn tại.")
    except Exception as e:
        print(f"Lỗi: {str(e)}")

    # Loại bỏ các từ ngừng từ văn bản

    words = content.split()
    filtered_words = [word for word in words if word.lower() not in stopwords_vi]




    # tom tat van ban
    text_to_summarize = content

    model = Summarizer()

    summary_dict = model(text_to_summarize)


    print("\n"
          "Tóm tắt văn bản:")
    print(summary_dict)

    return summary_dict
# Đọc văn bản từ một tệp
# with open("E:\\pythonProject\\Directory\\J.txt", "r", encoding="utf-8") as file:
# content = file.read()

# Tách văn bản thành danh sách các từ
# words = content.split()

# Tạo danh sách từ ngừng tiếng Việt (ví dụ)
# english_stopwords = set(stopwords.words('english'))

# Tạo từ điển để lưu số lần xuất hiện của các từ
# word_count_dict = defaultdict(int)

# Đếm số lần xuất hiện của các từ (loại bỏ từ ngừng)
# for word in words:
# Loại bỏ các ký tự đặc biệt và chuyển thành chữ thường để tránh phân biệt in hoa và thường

# Kiểm tra xem từ có trong danh sách từ ngừng không
# if word not in english_stopwords:
# word_count_dict[word] += 1

# In ra các từ xuất hiện nhiều nhất (top 10 ví dụ)
# top_words = sorted(word_count_dict.items(), key=lambda x: x[1], reverse=True)[:10]
# print("Top 10 từ xuất hiện nhiều nhất (loại bỏ từ ngừng):")
# for word, count in top_words:
# print(f"Từ '{word}' xuất hiện {count} lần trong văn bản.")
