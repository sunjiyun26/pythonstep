package com.inspur.pm4h2.chart;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.text.DecimalFormat;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.Vector;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import com.inspur.pm4h2.vo.chart.ColumnVO;
import com.inspur.pm4h2.vo.chart.PageVO;

//display WEB Report

public class ReportDisplay {
	public Vector<String> alltable;

	public ReportDisplay() {
	}

	// in:The path of Data File
	public ReportDisplay(String in) {
		File dataFilePath = new File(in);
		alltable = new Vector<String>();
		if (!dataFilePath.exists()) {
			System.out.println("This file " + in + " is not exit!");
			return;
		}

	}

	// report_file_path:The path of Data File
	// display original data file
	// public Vector displayReport(String report_file_path, String displayif) {
	// File dataFile = new File(report_file_path);
	// try {
	// BufferedReader br = new BufferedReader(new FileReader(dataFile));
	// String readDataline = "";
	// readDataline = br.readLine();
	// displayReportHead(readDataline);
	// int flag = 1;
	// do {
	// readDataline = br.readLine();
	// if (readDataline == null)
	// break;
	// displayReportData(readDataline, flag, displayif, null,null,null);
	// flag++;
	// } while (true);
	//
	// } catch (Exception e) {
	// System.out.println("Error occurs when reading data from file, "
	// + e.getMessage());
	// }
	// return alltable;
	// }

	// report_file_path:The path of Data File
	// display original data file
	// public String displayReportLine(String line, int flag, String displayif)
	// {
	// String lineStr = "";
	// try {
	// lineStr = displayReportData(line, flag, displayif, null,null,null);
	//
	// } catch (Exception e) {
	// System.out.println("Error occurs when reading data from file, "
	// + e.getMessage());
	// }
	// return lineStr;
	// }

	// report_file_path:The path of Data File
	// display original data file
	// 显示原始数据文件中的真实内容的报表
	public Vector displayRealReport(String report_file_path) {
		File dataFile = new File(report_file_path);
		try {
			BufferedReader br = new BufferedReader(new FileReader(dataFile));
			String readDataline = "";
			readDataline = br.readLine();
			displayReportHead(readDataline);
			int flag = 1;
			do {
				readDataline = br.readLine();
				if (readDataline == null)
					break;
				displayRealReportData(readDataline, flag);
				flag++;
			} while (true);

		} catch (Exception e) {
			System.out.println("Error occurs when reading data from file, " + e.getStackTrace());
		}
		return alltable;
	}

	// Display the head of report

	public void displayReportHead(String readDataline) {
		String[] reportHeadInfo = readDataline.split("\\|");
		String headInfo = "";
		if (reportHeadInfo.length != 0) {

			headInfo = headInfo + "<tr>";
			for (int i = 0; i < reportHeadInfo.length; i++) {
				headInfo = headInfo + "<td NOWRAP  align=left height=30 bgcolor=\"#6699CC\" ><font color=\"FFFFFF\">" + reportHeadInfo[i] + "111</font></td>";
			}
			headInfo = headInfo + "</tr>";
		}
		alltable.addElement(new String(headInfo));
		return;
	}

	// Display the content of report
	// 显示规定要显示的数据
	public String displayReportData(String readDataline, String[] xlmHead, List<ColumnVO> list, String[] blankInfo, int colorFlag, boolean isDisplayMenu, Map<String, String> hyperMap) {
		String[] reportDataInfo = readDataline.split("\\|", -1);
		HashMap<String, String> dataMap = new HashMap();
		for (int i = 0; i < xlmHead.length; i++) {
			//System.out.println(xlmHead[i]);
			dataMap.put(xlmHead[i].trim(), reportDataInfo[i]);
		}
		int i = 0;
		String dataInfo = "";
		// String color = (colorFlag%2 == 0)?"":"";
		if (colorFlag % 2 == 0) {
			dataInfo = dataInfo + "<tr onMouseOver=navbarOver2(this); onMouseOut=navbarOut2(this); onclick=oneClick2(this);";
			if (isDisplayMenu) {
				dataInfo += " oncontextmenu=showMenu(this);";
			}
			dataInfo += " bgcolor=#FFFFFF bordercolorlight=#000000>";

		} else {
			dataInfo = dataInfo + "<tr onMouseOver=navbarOver1(this); onMouseOut=navbarOut1(this); onclick=oneClick1(this);";
			if (isDisplayMenu) {
				dataInfo += " oncontextmenu=showMenu(this);";
			}
			dataInfo += "  bgcolor=#ECECFF bordercolorlight=#000000>";
		}

		for (ColumnVO columnVO : list) {
			//if (columnVO.getDisplay().equals("0")) {
			//	continue;
			//} else {
			String isDisplay = columnVO.getDisplay();
				String xmlHeadName = columnVO.getDatafield();
				if (dataMap.get(xmlHeadName).equals("") && !blankInfo[0].equals("")&& "1".equals(isDisplay)) {
					dataInfo = dataInfo + "<td NOWRAP id=" + (++i) + "_"+colorFlag +" class='tdContrast' blank='true' align=center bgcolor=" + blankInfo[0] + ">" + blankInfo[1] + "</td>";
				} else if (columnVO.getHighlightState().equals("1")&&"1".equals(isDisplay)) {
					HashMap<String[], String> highlightFormat = columnVO.getHighlightFormat();
					Set<Map.Entry<String[], String>> set = highlightFormat.entrySet();
					boolean flag = false;
					for (Map.Entry<String[], String> me : set) {
						String[] formatArr = me.getKey();
						System.out.println("formatArr.length" + formatArr.length);
						if (formatArr.length == 3) {
							flag = valiteHighlight(dataMap.get(formatArr[0]), formatArr[1], formatArr[2]);
						} else if (formatArr.length == 7) {
							boolean flag1 = valiteHighlight(dataMap.get(formatArr[0]), formatArr[1], formatArr[2]);
							boolean flag2 = valiteHighlight(dataMap.get(formatArr[4]), formatArr[5], formatArr[6]);
							flag = flag1 && flag2;
						} else {
							flag = false;
						}
						if (flag) {
							dataInfo = dataInfo + "<td NOWRAP id=" + (++i) + " class='tdContrast' align=center bgcolor=" + me.getValue() + ">" + dataMap.get(xmlHeadName) + "</td>";
							break;
						} else {
							dataInfo = dataInfo + "<td NOWRAP id=" + (++i) + " class='tdContrast' align=center >" + dataMap.get(xmlHeadName) + "</td>";
							break;
						}
					}
				} else {
						String formatType = columnVO.getFormatType();
						String parseFormat = columnVO.getParseFormatter();
						String displayFormat = columnVO.getDisplayFormatter();
						Map<String,String> formatMap = new HashMap<String, String>();
						formatMap.put("parseFormat", parseFormat);
						formatMap.put("displayFormat", displayFormat);
					String value = dataMap.get(xmlHeadName);
if(formatType!=null){
					value = formatterValue(formatType,formatMap,value);
				}
//					dataInfo = dataInfo + "<td NOWRAP id=" + (++i) + " class='tdContrast'";
if ("0".equals(isDisplay)) {
//					dataInfo += " tdhidden";
	                dataInfo = dataInfo + "<td NOWRAP id=" + (++i) + " class='tdContrast tdhidden'";
				}else{
					dataInfo = dataInfo + "<td NOWRAP id=" + (++i) + " class='tdContrast'";
				}
				if("-".equalsIgnoreCase(dataMap.get(xmlHeadName))||"".equalsIgnoreCase(dataMap.get(xmlHeadName))){
					dataInfo += ("' blank='true' ");
				}else{
					dataInfo += ("' blank='false' ");
				}
					if (isNumber(value)) {
						dataInfo+=(" align='right' >");
					} else {
						dataInfo+=(" align=center >");
					}
					if (hyperMap.containsKey(xmlHeadName) && !"-".equalsIgnoreCase(dataMap.get(xmlHeadName))) {
						String href = hyperMap.get(xmlHeadName);
						Pattern pattern = Pattern.compile("\\$\\[\\w+\\]");
						Matcher matcher = pattern.matcher(href);
						dataInfo += "<a href=\"javascript:void(0);\"";
						dataInfo += " url=\"http://";
						dataInfo += hyperMap.get(xmlHeadName);
						dataInfo += "\" target=\"_blank\" onclick=\"a_forward(this)\">";
						dataInfo += value;
						dataInfo += "</a></td>";
						if (matcher.find()) {
							dataInfo = dataInfo.replace("$[COLUMN]", dataMap.get(xmlHeadName));
						}
					} else {
						dataInfo += value + "</td>";
					}
				}
			}
		dataInfo = dataInfo + "</tr>";
		return dataInfo;
	}
private String formatterValue(String type,Map<String,String> format,String value){
		String parseFormat = format.get("parseFormat");
		String displayFormat = format.get("displayFormat");
		if("date".equalsIgnoreCase(type)){
			SimpleDateFormat pFormat = new SimpleDateFormat(parseFormat);
			SimpleDateFormat dFormat = new SimpleDateFormat(displayFormat);
			if(value.length()==9){
				value += "00000";
			}
			try {
				value = dFormat.format(pFormat.parse(value));
			} catch (ParseException e) {
				e.printStackTrace();
			}
		}else if("number".equalsIgnoreCase(type)){
			DecimalFormat decimalFormat = new DecimalFormat(displayFormat);
			value = decimalFormat.format(Double.valueOf(value));
		}
		return value;
	}
	private boolean isNumber(String value) {
		Pattern pattern = Pattern.compile("^(\\d+\\.{1}\\d*|(\\d{0,3}\\,{1})+\\d{3}|\\d+|(\\d{0,3}\\,{1})+\\d{3}\\.{1}\\d*|\\.{1}\\d+)$");
		Matcher matcher = pattern.matcher(value);
		return matcher.find();
	}
	// 校验是否满足高亮条件
	// 校验是否满足高亮条件
	public boolean valiteHighlight(String st, String com, String ed) {
		Double start = Double.parseDouble(st);
		Double end = Double.parseDouble(ed);
		String logic = com.trim();
		if (logic.equals(">")) {
			return start > end;
		} else if (logic.equals("<")) {
			return start < end;
		} else if (logic.equals(">=")) {
			return start >= end;
		} else if (logic.equals("<=")) {
			return start <= end;
		} else if (logic.equals("=")) {

			return start == end;
		} else if (logic.equals("!=")) {
			return start != end;
		} else {
			return false;
		}
	}

	public PageVO getPageInfo(String dataPath, String conditionPath) {
		PageVO pageVO = new PageVO();
		int currentPage = 1;
		int totalPage = 0;
		int totalRecords = -1;
		File dataFile = new File(dataPath);
		try {
			BufferedReader br = new BufferedReader(new FileReader(dataFile));

			String readDataline = "";

			ConditionAnalysis condition = new ConditionAnalysis(conditionPath);
			condition.setFormatPath(conditionPath);
			String head = condition.getReportHead().toString();
			if (head == null || head.equals("")) {

			} else {
				do {
					readDataline = br.readLine();
					if (readDataline == null || readDataline.equals(""))
						break;
					totalRecords++;
				} while (true);
				totalPage = totalRecords % 30 == 0 ? totalRecords / 30 : totalRecords / 30 + 1;
			}
			pageVO.setCurrentPage(currentPage);
			pageVO.setTotalPage(totalPage);
			pageVO.setTotalRecords(totalRecords);
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return pageVO;

	}

	// 显示数据文件的原始数据
	public void displayRealReportData(String readDataline, int colorFlag) {

		String[] reportDataInfo = readDataline.split("\\|");
		String dataInfo = "";
		String color = (colorFlag % 2 == 0) ? "#ECECFF" : "#FFFFFF";
		if (reportDataInfo.length != 0) {
			dataInfo = dataInfo + "<tr>";
			for (int i = 0; i < reportDataInfo.length; i++) {
				dataInfo = dataInfo + "<td NOWRAP  align=center height=30 bgcolor=\"" + color + "\" >" + reportDataInfo[i] + "</td>";
			}
			dataInfo = dataInfo + "</tr>";
		}
		alltable.addElement(new String(dataInfo));
		return;
	}

	private String pagetypestr1[] = { "<script language=JavaScript>", "var clrOve1 = '#6395d1';", "var clrOut1 = '#efefef';", "var clrCli1 = '#99a5ac';", "", "function navbarOver1(src){", "if (src.bgColor == clrCli1){", "  }else{", "  if (!src.contains(event.fromElement)){", "    src.style.cursor = 'hand';", "    src.bgColor = clrOve1;", "    src.bordercolorlight = '#FFFFFF';", "  }", "}", "}", "", "function navbarOut1(src){", "if (src.bgColor == clrCli1){", "  }else{", "  if (!src.contains(event.toElement)){", "    src.style.cursor = 'default';", "    src.bgColor = clrOut1;", "    src.bordercolorlight = '#FFFFFF';", "  }", "}", "}", "", "function oneClick1(src){", "if(src.bgColor == clrCli1){", "  if (!src.contains(event.fromElement)){", "    src.bgColor = clrOut1;",
			"    src.bordercolorlight = '#FFFFFF';", "  }", "}else{", "  if (!src.contains(event.fromElement)){", "    src.bgColor = clrCli1;", "    src.bordercolorlight = '#FFFFFF';", "  }", "}", "}", "var clrOve2 = '#6395d1';", "var clrOut2 = '#ffffff';", "var clrCli2 = '#99a5ac';", "", "function navbarOver2(src){", "if (src.bgColor == clrCli2){", "  }else{", "  if (!src.contains(event.fromElement)){", "    src.style.cursor = 'hand';", "    src.bgColor = clrOve2;", "    src.bordercolorlight = '#FFFFFF';", "  }", "}", "}", "", "function navbarOut2(src){", "if (src.bgColor == clrCli2){", "  }else{", "  if (!src.contains(event.toElement)){", "    src.style.cursor = 'default';", "    src.bgColor = clrOut2;", "    src.bordercolorlight = '#FFFFFF';", "  }", "}", "}", "",
			"function oneClick2(src){", "if(src.bgColor == clrCli2){", "  if (!src.contains(event.fromElement)){", "    src.bgColor = clrOut2;", "    src.bordercolorlight = '#FFFFFF';", "  }", "}else{", "  if (!src.contains(event.fromElement)){", "    src.bgColor = clrCli2;", "    src.bordercolorlight = '#FFFFFF';", "  }", "}", "}", "</script>" };

}
