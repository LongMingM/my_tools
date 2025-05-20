// Consol.cpp : 此文件包含 "main" 函数。程序执行将在此处开始并结束。
//
#include"Consol.h"


void splitChannelDetector::split_channel(string& path)
{
	vector<string> filenames;
	glob(path, filenames, false);
	if (filenames.size() == 0)
	{
		cerr << "That's no file in" << path << endl;
		exit(0);
	}
	for (int i = 0; i < filenames.size(); i++)
	{
		cout << "正在处理图像：" + filenames[i] << endl;
		Mat src = imread(filenames[i]);
		if (src.empty())
		{
			cerr << "read image failed!" << endl;
			exit(0);
		}
		//RGB
		size_t index = filenames[i].find_last_of("\\");
		string img_name = filenames[i].substr(index + 1);
		string new_name_R = write_path_R + img_name;
		string new_name_G = write_path_G + img_name;
		string new_name_B = write_path_B + img_name;

		//HSV
		string new_name_HSV = write_path_HSV + img_name;
		string new_name_H = write_path_H + img_name;
		string new_name_S = write_path_S + img_name;
		string new_name_V = write_path_V + img_name;

		//lab
		string new_name_lab = write_path_lab + img_name;
		string new_name_l = write_path_l + img_name;
		string new_name_a = write_path_a + img_name;
		string new_name_b = write_path_b + img_name;

		//HLS
		string new_name_HLS = write_path_HLS + img_name;
		string new_name_HLS_H = write_path_HLS_H + img_name;
		string new_name_HLS_L = write_path_HLS_L + img_name;
		string new_name_HLS_S = write_path_HLS_S + img_name;


		//组合通道
		// b / r + g * 150
		string new_name_B_GR = write_path_BdivGR + img_name;

		// r / b + g * 150
		string new_name_R_BG = write_path_RdivBG + img_name;

		// b + g + r
		string new_name_BGR = write_path_BGR + img_name;

		//~r + b + g
		string new_name_notRBG = write_path_notRBG + img_name;

		//~r + g / b *100
		string new_name_notRB_G = write_path_notRB_G + img_name;

		//threshold value
		string new_name_thres_Value = write_path_thres_Value + img_name;

		//R +G
		string new_name_RG = write_path_RG + img_name;

		//V-B
		string new_name_V_B = write_path_V_B + img_name;

		//BPlusG
		string new_name_BPlusG = write_path_BPlusG + img_name;

		//R + 2*G
		string new_nameR2G = write_path_R2G + img_name;

		//B_100Plus2G
		string new_nameB_100Plus2G = write_path_B_100Plus2G + img_name;

		//L_b
		string new_nameL_b = write_path_L_b + img_name;

		//Sobel
		string new_nameSobel = write_path_Sobel + img_name;

		//通过颜色通道进行抠图
		vector<Mat> bgrchannels;
		//效果最好的是value通道 
		//得到颜色通道，从找出最好的分割图像区域的通道
		split(src, bgrchannels);
		Mat blue_channel = bgrchannels[0];
		Mat green_channel = bgrchannels[1];
		Mat red_channel = bgrchannels[2];
		imwrite(new_name_B, blue_channel);
		imwrite(new_name_G, green_channel);
		imwrite(new_name_R, red_channel);

		//转成HSV空间，是因为RGB通道，缺陷难以分辨
		Mat hsv;
		vector<Mat> hsvchannels;
		cvtColor(src, hsv, COLOR_BGR2HSV);
		split(hsv, hsvchannels);
		Mat hue_channel = hsvchannels[0];
		Mat sat_channel = hsvchannels[1];
		Mat value_channel = hsvchannels[2];
		imwrite(new_name_HSV, hsv);
		imwrite(new_name_H, hue_channel);
		imwrite(new_name_S, sat_channel);
		imwrite(new_name_V, value_channel);

		//转换到lab空间
		Mat lab;
		vector<Mat> labchannels;
		cvtColor(src, lab, COLOR_BGR2Lab);
		split(lab, labchannels);
		Mat l_channel = labchannels[0];
		Mat a_channel = labchannels[1];
		Mat b_channel = labchannels[2];
		imwrite(new_name_lab, lab);
		imwrite(new_name_l, l_channel);
		imwrite(new_name_a, a_channel);
		imwrite(new_name_b, b_channel);

		//转换到HSI空间
		Mat hls;
		vector<Mat> hlschannels;
		cvtColor(src, hls, COLOR_BGR2HLS);
		split(hls, hlschannels);
		Mat hls_h_channel = hlschannels[0];
		Mat hls_l_channel = hlschannels[1];
		Mat hls_s_channel = hlschannels[2];
		imwrite(new_name_HLS, hls);
		imwrite(new_name_HLS_H, hls_h_channel);
		imwrite(new_name_HLS_S, hls_l_channel);
		imwrite(new_name_HLS_L, hls_s_channel);


		//组合通道

		// B / ( G + R )
		Mat B_GR_channel = (blue_channel) / (red_channel + green_channel) * 150;
		imwrite(new_name_B_GR, B_GR_channel);

		//R / (B + G)
		Mat R_BG_channel = (red_channel / (blue_channel + green_channel)) * 150;
		imwrite(new_name_R_BG, R_BG_channel);
		
		// B + G + R
		Mat BGR_channel = blue_channel + green_channel + red_channel;
		imwrite(new_name_BGR, BGR_channel);

		//~R + B + G
		Mat RedInvert = red_channel.clone();
		RedInvert = ~RedInvert;
		Mat notRGB_channel = RedInvert + blue_channel + green_channel;
		imwrite(new_name_notRBG, notRGB_channel);

		//~R / (B + G) * 100
		Mat notRB_G_channel = RedInvert / (blue_channel + green_channel) * 100;
		imwrite(new_name_notRB_G, notRB_G_channel);
		
		//threshold Value
		Mat threshold_value;
		cv::threshold(value_channel, threshold_value, 20, 255, THRESH_BINARY);
		imwrite(new_name_thres_Value, threshold_value);

		//Sobel
		Mat sobelImg;
		Mat normalizeImg;
		get_grad_sobel(value_channel, sobelImg, 'd');
		cv::normalize(sobelImg, normalizeImg, 255, 0, NORM_MINMAX);

		Mat sobelThresImg;
		threshold(normalizeImg, sobelThresImg, 25, 255, THRESH_BINARY);
		imwrite(new_nameSobel, sobelThresImg);


		//R + G
		Mat RG = red_channel + green_channel;
		imwrite(new_name_RG, RG);

		//V_B
		Mat V_B = value_channel - blue_channel;
		imwrite(new_name_V_B, V_B);

		//V_B
		Mat BPlusG = blue_channel + green_channel;
		imwrite(new_name_BPlusG, BPlusG);

		//R + 2 * G
		Mat R2G = red_channel + 2 * green_channel;
		imwrite(new_nameR2G, R2G);

		//B_100Plus2G
		Mat B_100Plus2G = blue_channel - 100 + 2 * green_channel;
		imwrite(new_nameB_100Plus2G, B_100Plus2G);

		//L_b
		Mat L_b = l_channel - b_channel;
		imwrite(new_nameL_b, L_b);

		//HSI

		
	}
	cout << "图像分割结束" << endl;
	return;
}

void splitChannelDetector::initWritePath(string& path)
{
	head = path + "\\splitChannel";

	write_path_R = head + "\\R\\";
	write_path_G = head + "\\G\\";
	write_path_B = head + "\\B\\";
	allImgWritePath.push_back(write_path_R);
	allImgWritePath.push_back(write_path_G);
	allImgWritePath.push_back(write_path_B);

	write_path_HSV = head + "\\HSV\\";
	write_path_H = head +  "\\H\\";
	write_path_S = head + "\\S\\";
	write_path_V = head +  "\\V\\";
	allImgWritePath.push_back(write_path_HSV);
	allImgWritePath.push_back(write_path_H);
	allImgWritePath.push_back(write_path_S);
	allImgWritePath.push_back(write_path_V);

	write_path_l = head + "\\lab_l\\";
	write_path_a = head + "\\lab_a\\";
	write_path_b = head + "\\lab_b\\";
	write_path_lab = head + "\\lab\\";
	allImgWritePath.push_back(write_path_l);
	allImgWritePath.push_back(write_path_a);
	allImgWritePath.push_back(write_path_b);
	allImgWritePath.push_back(write_path_lab);

	write_path_HLS_H = head +  "\\HLS_H\\";
	write_path_HLS_L = head +  "\\HLS_L\\";
	write_path_HLS_S = head +  "\\HLS_S\\";
	write_path_HLS = head + "\\HLS\\";
	allImgWritePath.push_back(write_path_HLS_H);
	allImgWritePath.push_back(write_path_HLS_L);
	allImgWritePath.push_back(write_path_HLS_S);
	allImgWritePath.push_back(write_path_HLS);

	write_path_Sobel = head +  "\\Sobel\\";
	allImgWritePath.push_back(write_path_Sobel);

	//组合通道
	//B / (G + R)
	write_path_BdivGR = head +  "\\B_GR\\";
	allImgWritePath.push_back(write_path_BdivGR);

	//R / (B + G)
	write_path_RdivBG = head +  "\\R_BG\\";
	allImgWritePath.push_back(write_path_RdivBG);

	// r+ b + g
	write_path_BGR = head +  "\\BGR\\";
	allImgWritePath.push_back(write_path_BGR);
	//~r + b + g
	write_path_notRBG = head + "\\notRGB\\";
	allImgWritePath.push_back(write_path_notRBG);
	//~r + g / b *100
	write_path_notRB_G = head + "\\notRB_G\\";
	allImgWritePath.push_back(write_path_notRB_G);
	//threshold value
	write_path_thres_Value = head + "\\thres_Value\\";
	allImgWritePath.push_back(write_path_thres_Value);
	//R + G
	write_path_RG = head +  "\\RG\\";
	allImgWritePath.push_back(write_path_RG);
	//bianjiaofahong
	write_path_V_B = head +  "\\V_B\\";
	allImgWritePath.push_back(write_path_V_B);
	//B+G
	write_path_BPlusG = head +  "\\BPlusG\\";
	allImgWritePath.push_back(write_path_BPlusG);
	//R+ 2*G
	write_path_R2G = head +  "\\R2G\\";
	allImgWritePath.push_back(write_path_R2G);
	//B - 100 + 2 * G
	write_path_B_100Plus2G = head + "\\B_100Plus2G\\";
	allImgWritePath.push_back(write_path_B_100Plus2G);
	//Lab_l - Lab_b
	write_path_L_b = head + "\\L_b\\";
	allImgWritePath.push_back(write_path_L_b);
	return;
}

void splitChannelDetector::createFile()
{
	LPCSTR headFile = head.c_str();
	CreateDirectoryA(headFile, NULL);
	for (auto curFile: allImgWritePath)
	{
		LPCSTR path = curFile.c_str();
		CreateDirectoryA(path, NULL);
	}
}

int splitChannelDetector::get_grad_sobel(const Mat &gray, Mat&grad, char type)
{
	int ret = 0;
	int scale = 1;
	int delta = 0;
	int ddepth = CV_16S;
	Mat src_gray = gray.clone();
	Mat dst;
	/// 创建 grad_x 和 grad_y 矩阵
	Mat grad_x, grad_y;
	Mat abs_grad_x, abs_grad_y;

	/// 求 X方向梯度
	//Scharr( src_gray, grad_x, ddepth, 1, 0, scale, delta, BORDER_DEFAULT );
	Sobel(src_gray, grad_x, ddepth, 1, 0, 3, scale, delta, BORDER_DEFAULT);
	convertScaleAbs(grad_x, abs_grad_x);

	/// 求Y方向梯度
	//Scharr( src_gray, grad_y, ddepth, 0, 1, scale, delta, BORDER_DEFAULT );
	Sobel(src_gray, grad_y, ddepth, 0, 1, 3, scale, delta, BORDER_DEFAULT);
	convertScaleAbs(grad_y, abs_grad_y);

	/// 合并梯度(近似)
	addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0, dst);


	switch (type)
	{
	case 'x':
		grad = abs_grad_x.clone();
		break;
	case 'y':
		grad = abs_grad_y.clone();
		break;
	case 'd':
		grad = dst.clone();
		break;
	default:
		grad = dst.clone();
		break;
	}
	return ret;
}


int main()
{
	
	//string path = "E:\\E_Problems_solve\\2024.06.12_西咸隆基背景问题导致误检碎片\\17误判\\B\\";   
	string path;
	cout << "输入图像路径" << endl;
	cin >> path;
	//string path = "D:\\seafile_data\\Seafile\\正膜mark点\\test_img\\";        
	//在当前路径下创建文件夹
	//path.replace(path.begin(), path.end(), "\\", "\\");
	splitChannelDetector splitChannelD;
	splitChannelD.initWritePath(path);
	//创建对应的文件夹
	splitChannelD.createFile();
	splitChannelD.split_channel(path);
	system("pause");
	return 0;
}

// 运行程序: Ctrl + F5 或调试 >“开始执行(不调试)”菜单
// 调试程序: F5 或调试 >“开始调试”菜单

// 入门使用技巧: 
//   1. 使用解决方案资源管理器窗口添加/管理文件
//   2. 使用团队资源管理器窗口连接到源代码管理
//   3. 使用输出窗口查看生成输出和其他消息
//   4. 使用错误列表窗口查看错误
//   5. 转到“项目”>“添加新项”以创建新的代码文件，或转到“项目”>“添加现有项”以将现有代码文件添加到项目
//   6. 将来，若要再次打开此项目，请转到“文件”>“打开”>“项目”并选择 .sln 文件
