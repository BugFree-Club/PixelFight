using System;
using Newtonsoft.Json;
public class PixelFightClient {
    private string serverIp;
    private string serverPort;
    private string usrName;
    private string loginId;
    private string pfMap;
    public PixelFightClient(String usrName, String ip, String port) {
        ServerIp = ip;
        ServerPort = port;
        UsrName = usrName;
        LoginId = null;
        PfMap = null;
    }
    public PixelFightClient() { }
    public string ServerIp { get => serverIp; set => serverIp = value; }
    public string ServerPort { get => serverPort; set => serverPort = value; }
    public string UsrName { get => usrName; set => usrName = value; }
    public string LoginId { get => loginId; set => loginId = value; }
    public string PfMap { get => pfMap; set => pfMap = value; }
    public string ClientSocket;
    public void Request(String msg) { }
    public void LoginReuest() { }


}