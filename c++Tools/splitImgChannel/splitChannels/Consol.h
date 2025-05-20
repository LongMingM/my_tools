#pragma once
#include<opencv2/opencv.hpp>
#include<opencv2/opencv_modules.hpp>
#include <iostream>
#include<filesystem>
#include<string>
#include <windows.h>  // For Windows API
using namespace cv;
using namespace std;


class splitChannelDetector
{
private:

	string write_path_R;
	string write_path_G;
	string write_path_B;

	string write_path_HSV;
	string write_path_H;
	string write_path_S;
	string write_path_V;

	string write_path_l;
	string write_path_a;
	string write_path_b;
	string write_path_lab;

	string write_path_HLS_H;
	string write_path_HLS_L;
	string write_path_HLS_S;
	string write_path_HLS;

	string write_path_Sobel;

	//组合通道
	//B / (G + R)
	string write_path_BdivGR;

	//R / (B + G)
	string write_path_RdivBG;

	// r+ b + g
	string write_path_BGR;

	//~r + b + g
	string write_path_notRBG;

	//~r + g / b *100
	string write_path_notRB_G;

	//threshold value
	string write_path_thres_Value;

	//R + G
	string write_path_RG;

	//bianjiaofahong
	string write_path_V_B;

	//B+G
	string write_path_BPlusG;

	//R+ 2*G
	string write_path_R2G;

	//B - 100 + 2 * G
	string write_path_B_100Plus2G;

	//Lab_l - Lab_b
	string write_path_L_b;
	vector<string> allImgWritePath;
	string head;
public:
	void initWritePath(string& path);
	void split_channel(string& path);
	void createFile();
	int get_grad_sobel(const Mat &gray, Mat&grad, char type);
};
