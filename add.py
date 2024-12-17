# -*- coding: utf-8 -*-

mainscript = """class
 refid "Client"
 instance QName(PackageNamespace(""), "Client")
  extends QName(PackageNamespace(""), "Object")
  flag SEALED
  flag PROTECTEDNS
  protectedns ProtectedNamespace("Client")
  iinit
   refid "Client/iinit"
   body
    maxstack 1
    localcount 1
    initscopedepth 4
    maxscopedepth 5
    code
     getlocal0
     pushscope

     getlocal0
     constructsuper      0

     returnvoid
    end ; code
   end ; body
  end ; method
 end ; instance
 cinit
  refid "Client/cinit"
  body
   maxstack 2
   localcount 1
   initscopedepth 3
   maxscopedepth 4
   code
    getlocal0
    pushscope

    findproperty        QName(PackageNamespace(""), "maps")
    findpropstrict      QName(PackageNamespace("flash.utils"), "Dictionary")
    constructprop       QName(PackageNamespace("flash.utils"), "Dictionary"), 0
    setproperty         QName(PackageNamespace(""), "maps")

    findproperty        QName(PackageNamespace(""), "main")
    pushstring          "mainclass"
    setproperty         QName(PackageNamespace(""), "main")

    findproperty        QName(PackageNamespace(""), "bulle")
    pushstring          "bulleclass"
    setproperty         QName(PackageNamespace(""), "bulle")

    findproperty        QName(PackageNamespace(""), "socket")
    pushstring          "socketclass"
    setproperty         QName(PackageNamespace(""), "socket")

    findproperty        QName(PackageNamespace(""), "packetId")
    pushstring          "packeteclass"
    setproperty         QName(PackageNamespace(""), "packetId")

    findproperty        QName(PackageNamespace(""), "recvPacketFunction")
    pushstring          "recvpacketclass"
    setproperty         QName(PackageNamespace(""), "recvPacketFunction")

    findproperty        QName(PackageNamespace(""), "autoplay")
    pushtrue
    setproperty         QName(PackageNamespace(""), "autoplay")

    findproperty        QName(PackageNamespace(""), "bornPeriod")
    pushdouble          2.9
    setproperty         QName(PackageNamespace(""), "bornPeriod")

    findproperty        QName(PackageNamespace(""), "roundCode")
    pushbyte            0
    setproperty         QName(PackageNamespace(""), "roundCode")
    
    findproperty        QName(PackageNamespace(""), "map_xml")
    pushstring          ""
    setproperty         QName(PackageNamespace(""), "map_xml")

    returnvoid
   end ; code
  end ; body
 end ; method
 trait slot QName(PackageNamespace(""), "mapCount") slotid 1 type QName(PackageNamespace(""), "int") end
 trait slot QName(PackageNamespace(""), "maps") slotid 2 type QName(PackageNamespace("flash.utils"), "Dictionary") end
 trait slot QName(PackageNamespace(""), "loader") slotid 3 type QName(PackageNamespace("flash.net"), "URLLoader") end
 trait slot QName(PackageNamespace(""), "connectionClass") slotid 4 type QName(PackageNamespace(""), "Object") end
 trait slot QName(PackageNamespace(""), "main") slotid 5 type QName(PackageNamespace(""), "String") value Utf8("mainclass") end
 trait slot QName(PackageNamespace(""), "bulle") slotid 6 type QName(PackageNamespace(""), "String") value Utf8("bulleclass") end
 trait slot QName(PackageNamespace(""), "socket") slotid 7 type QName(PackageNamespace(""), "String") value Utf8("socketclass") end
 trait slot QName(PackageNamespace(""), "packetId") slotid 8 type QName(PackageNamespace(""), "String") value Utf8("packeteclass") end
 trait slot QName(PackageNamespace(""), "recvClass") slotid 9 type QName(PackageNamespace(""), "Object") end
 trait slot QName(PackageNamespace(""), "recvPacketFunction") slotid 10 type QName(PackageNamespace(""), "String") value Utf8("recvpacketclass") end
 trait slot QName(PackageNamespace(""), "autoplay") slotid 11 type QName(PackageNamespace(""), "Boolean") value False() end
 trait slot QName(PackageNamespace(""), "bornPeriod") slotid 12 type QName(PackageNamespace(""), "Number") value Double(2.9) end
 trait slot QName(PackageNamespace(""), "roundCode") slotid 13 type QName(PackageNamespace(""), "int") value Integer(0) end
 trait slot QName(PackageNamespace(""), "playerCode") slotid 14 type QName(PackageNamespace(""), "int") end
 trait slot QName(PackageNamespace(""), "map_xml") slotid 15 type QName(PackageNamespace(""), "String") value Utf8("") end
 trait slot QName(PackageNamespace(""), "iden") slotid 16 type QName(PackageNamespace(""), "int") value Integer(1) end
 trait method QName(PackageNamespace(""), "downloadMaps") flag FINAL dispid 3
  method
   refid "Client/downloadMaps"
   returns QName(PackageNamespace(""), "void")
   body
    maxstack 3
    localcount 1
    initscopedepth 3
    maxscopedepth 4
    code
     getlocal0
     pushscope

     getlex              QName(PackageNamespace(""), "Client")
     findpropstrict      QName(PackageNamespace("flash.net"), "URLLoader")
     constructprop       QName(PackageNamespace("flash.net"), "URLLoader"), 0
     setproperty         QName(PackageNamespace(""), "loader")

     getlex              QName(PackageNamespace(""), "Client")
     getproperty         QName(PackageNamespace(""), "loader")
     getlex              QName(PackageNamespace("flash.net"), "URLLoaderDataFormat")
     getproperty         QName(PackageNamespace(""), "TEXT")
     setproperty         QName(PackageNamespace(""), "dataFormat")

     getlex              QName(PackageNamespace("flash.system"), "Security")
     pushstring          "*"
     callpropvoid        QName(PackageNamespace(""), "allowDomain"), 1

     getlex              QName(PackageNamespace(""), "Client")
     getproperty         QName(PackageNamespace(""), "loader")
     getlex              QName(PackageNamespace("flash.events"), "Event")
     getproperty         QName(PackageNamespace(""), "COMPLETE")
     getlex              QName(PackageNamespace(""), "Client")
     getproperty         QName(PackageNamespace(""), "mapsDownloaded")
     callpropvoid        QName(PackageNamespace(""), "addEventListener"), 2

     getlex              QName(PackageNamespace(""), "Client")
     getproperty         QName(PackageNamespace(""), "loader")
     findpropstrict      QName(PackageNamespace("flash.net"), "URLRequest")
     pushstring          "http://127.0.0.1/packets"
     constructprop       QName(PackageNamespace("flash.net"), "URLRequest"), 1
     callpropvoid        QName(PackageNamespace(""), "load"), 1

     returnvoid
    end ; code
   end ; body
  end ; method
 end ; trait
 trait method QName(PackageNamespace(""), "mapsDownloaded") flag FINAL dispid 4
  method
   refid "Client/mapsDownloaded"
   param QName(PackageNamespace("flash.events"), "Event")
   returns QName(PackageNamespace(""), "void")
   body
    maxstack 4
    localcount 7
    initscopedepth 3
    maxscopedepth 4
    code
     getlocal0
     pushscope

     pushbyte            0
     setlocal            4

     pushbyte            0
     setlocal            5

     pushnull
     coerce              QName(PackageNamespace("flash.utils"), "ByteArray")
     setlocal            6

     getlex              QName(PackageNamespace(""), "Client")
     getlex              QName(PackageNamespace(""), "Client")
     getproperty         QName(PackageNamespace(""), "loader")
     getproperty         QName(PackageNamespace(""), "data")
     callproperty        QName(PackageNamespace(""), "b64decode"), 1
     coerce              QName(PackageNamespace("flash.utils"), "ByteArray")
     setlocal2

     getlocal2
     pushstring          "zlib"
     callpropvoid        QName(PackageNamespace(""), "uncompress"), 1

     getlex              QName(PackageNamespace(""), "Client")
     getlocal2
     callproperty        QName(PackageNamespace(""), "readInt"), 0
     setproperty         QName(PackageNamespace(""), "mapCount")

     pushbyte            0
     setlocal3

     jump                L50

L26:
     label
     getlocal2
     callproperty        QName(PackageNamespace(""), "readInt"), 0
     convert_i
     setlocal            4

     getlocal2
     callproperty        QName(PackageNamespace(""), "readInt"), 0
     convert_i
     setlocal            5

     findpropstrict      QName(PackageNamespace("flash.utils"), "ByteArray")
     constructprop       QName(PackageNamespace("flash.utils"), "ByteArray"), 0
     coerce              QName(PackageNamespace("flash.utils"), "ByteArray")
     setlocal            6

     getlocal2
     getlocal            6
     pushbyte            0
     getlocal            5
     callpropvoid        QName(PackageNamespace(""), "readBytes"), 3

     getlex              QName(PackageNamespace(""), "Client")
     getproperty         QName(PackageNamespace(""), "maps")
     getlocal            4
     getlocal            6
     setproperty         MultinameL([PrivateNamespace(null, "Client#0"), PackageNamespace(""), PrivateNamespace(null, "Client#1"), PackageInternalNs(""), Namespace("http://adobe.com/AS3/2006/builtin"), ProtectedNamespace("Client"), StaticProtectedNs("Client")])

     inclocal_i          3
L50:
     getlocal3
     getlex              QName(PackageNamespace(""), "Client")
     getproperty         QName(PackageNamespace(""), "mapCount")
     iflt                L26

     returnvoid
    end ; code
   end ; body
  end ; method
 end ; trait
 trait method QName(PackageNamespace(""), "sendPacket") flag FINAL dispid 5
  method
   refid "Client/sendPacket"
   param QName(PackageNamespace("flash.utils"), "ByteArray")
   param QName(PackageNamespace(""), "String")
   returns QName(PackageNamespace(""), "void")
   flag HAS_OPTIONAL
   optional Utf8("bulle")
   body
    maxstack 4
    localcount 7
    initscopedepth 3
    maxscopedepth 4
    code
     getlocal0
     pushscope

     getlex              QName(PackageNamespace(""), "Client")
     getproperty         QName(PackageNamespace(""), "connectionClass")
     getlex              QName(PackageNamespace(""), "Client")
     getlocal2
     getproperty         MultinameL([PrivateNamespace(null, "Client#0"), PackageNamespace(""), PrivateNamespace(null, "Client#1"), PackageInternalNs(""), Namespace("http://adobe.com/AS3/2006/builtin"), ProtectedNamespace("Client"), StaticProtectedNs("Client")])
     getproperty         MultinameL([PrivateNamespace(null, "Client#0"), PackageNamespace(""), PrivateNamespace(null, "Client#1"), PackageInternalNs(""), Namespace("http://adobe.com/AS3/2006/builtin"), ProtectedNamespace("Client"), StaticProtectedNs("Client")])
     coerce              QName(PackageNamespace(""), "Object")
     setlocal3

     findpropstrict      QName(PackageNamespace("flash.utils"), "ByteArray")
     constructprop       QName(PackageNamespace("flash.utils"), "ByteArray"), 0
     coerce              QName(PackageNamespace("flash.utils"), "ByteArray")
     setlocal            4

     getlocal1
     getproperty         QName(PackageNamespace(""), "length")
     convert_i
     dup
     setlocal            5

     pushbyte            7
     urshift
     convert_i
     setlocal            6

     jump                L40

L24:
     label
     getlocal            4
     getlocal            5
     pushbyte            127
     bitand
     pushshort           128
     bitor
     callpropvoid        QName(PackageNamespace(""), "writeByte"), 1

     getlocal            6
     convert_i
     setlocal            5

     getlocal            6
     pushbyte            7
     urshift
     convert_i
     setlocal            6

L40:
     getlocal            6
     pushbyte            0
     ifne                L24

     getlocal            4
     getlocal            5
     pushbyte            127
     bitand
     callpropvoid        QName(PackageNamespace(""), "writeByte"), 1

     getlocal            4
     getlocal3
     getlex              QName(PackageNamespace(""), "Client")
     getproperty         QName(PackageNamespace(""), "packetId")
     getproperty         MultinameL([PrivateNamespace(null, "Client#0"), PackageNamespace(""), PrivateNamespace(null, "Client#1"), PackageInternalNs(""), Namespace("http://adobe.com/AS3/2006/builtin"), ProtectedNamespace("Client"), StaticProtectedNs("Client")])
     callpropvoid        QName(PackageNamespace(""), "writeByte"), 1

     getlocal3
     getlex              QName(PackageNamespace(""), "Client")
     getproperty         QName(PackageNamespace(""), "packetId")
     getlocal3
     getlex              QName(PackageNamespace(""), "Client")
     getproperty         QName(PackageNamespace(""), "packetId")
     getproperty         MultinameL([PrivateNamespace(null, "Client#0"), PackageNamespace(""), PrivateNamespace(null, "Client#1"), PackageInternalNs(""), Namespace("http://adobe.com/AS3/2006/builtin"), ProtectedNamespace("Client"), StaticProtectedNs("Client")])
     pushbyte            1
     add
     pushbyte            100
     modulo
     setproperty         MultinameL([PrivateNamespace(null, "Client#0"), PackageNamespace(""), PrivateNamespace(null, "Client#1"), PackageInternalNs(""), Namespace("http://adobe.com/AS3/2006/builtin"), ProtectedNamespace("Client"), StaticProtectedNs("Client")])

     getlocal3
     getlex              QName(PackageNamespace(""), "Client")
     getproperty         QName(PackageNamespace(""), "socket")
     getproperty         MultinameL([PrivateNamespace(null, "Client#0"), PackageNamespace(""), PrivateNamespace(null, "Client#1"), PackageInternalNs(""), Namespace("http://adobe.com/AS3/2006/builtin"), ProtectedNamespace("Client"), StaticProtectedNs("Client")])
     getlocal            4
     callpropvoid        Multiname("writeBytes", [PrivateNamespace(null, "Client#0"), PackageNamespace(""), PrivateNamespace(null, "Client#1"), PackageInternalNs(""), Namespace("http://adobe.com/AS3/2006/builtin"), ProtectedNamespace("Client"), StaticProtectedNs("Client")]), 1

     getlocal3
     getlex              QName(PackageNamespace(""), "Client")
     getproperty         QName(PackageNamespace(""), "socket")
     getproperty         MultinameL([PrivateNamespace(null, "Client#0"), PackageNamespace(""), PrivateNamespace(null, "Client#1"), PackageInternalNs(""), Namespace("http://adobe.com/AS3/2006/builtin"), ProtectedNamespace("Client"), StaticProtectedNs("Client")])
     getlocal1
     callpropvoid        Multiname("writeBytes", [PrivateNamespace(null, "Client#0"), PackageNamespace(""), PrivateNamespace(null, "Client#1"), PackageInternalNs(""), Namespace("http://adobe.com/AS3/2006/builtin"), ProtectedNamespace("Client"), StaticProtectedNs("Client")]), 1

     getlocal3
     getlex              QName(PackageNamespace(""), "Client")
     getproperty         QName(PackageNamespace(""), "socket")
     getproperty         MultinameL([PrivateNamespace(null, "Client#0"), PackageNamespace(""), PrivateNamespace(null, "Client#1"), PackageInternalNs(""), Namespace("http://adobe.com/AS3/2006/builtin"), ProtectedNamespace("Client"), StaticProtectedNs("Client")])
     callpropvoid        Multiname("flush", [PrivateNamespace(null, "Client#0"), PackageNamespace(""), PrivateNamespace(null, "Client#1"), PackageInternalNs(""), Namespace("http://adobe.com/AS3/2006/builtin"), ProtectedNamespace("Client"), StaticProtectedNs("Client")]), 0

     returnvoid
    end ; code
   end ; body
  end ; method
 end ; trait
 trait method QName(PackageNamespace(""), "sendMessage") flag FINAL dispid 6
  method
   refid "Client/sendMessage"
   param QName(PackageNamespace(""), "String")
   returns QName(PackageNamespace(""), "void")
   body
    maxstack 3
    localcount 4
    initscopedepth 3
    maxscopedepth 4
    code
     getlocal0
     pushscope

     findpropstrict      QName(PackageNamespace("flash.utils"), "ByteArray")
     constructprop       QName(PackageNamespace("flash.utils"), "ByteArray"), 0
     coerce              QName(PackageNamespace("flash.utils"), "ByteArray")
     setlocal2

     getlocal2
     pushbyte            6
     callpropvoid        QName(PackageNamespace(""), "writeByte"), 1

     getlocal2
     pushbyte            9
     callpropvoid        QName(PackageNamespace(""), "writeByte"), 1

     getlocal2
     getlocal1
     callpropvoid        QName(PackageNamespace(""), "writeUTF"), 1

     getlex              QName(PackageNamespace(""), "Client")
     getproperty         QName(PackageNamespace(""), "recvClass")
     dup
     setlocal3

     getlex              QName(PackageNamespace(""), "Client")
     getproperty         QName(PackageNamespace(""), "recvPacketFunction")
     getproperty         MultinameL([PrivateNamespace(null, "Client#0"), PackageNamespace(""), PrivateNamespace(null, "Client#1"), PackageInternalNs(""), Namespace("http://adobe.com/AS3/2006/builtin"), ProtectedNamespace("Client"), StaticProtectedNs("Client")])
     getlocal3
     getlocal2
     call                1
     pop
     kill                3
     returnvoid
    end ; code
   end ; body
  end ; method
 end ; trait
 trait method QName(PackageNamespace(""), "crouch") flag FINAL dispid 7
  method
   refid "Client/crouch"
   param QName(PackageNamespace(""), "int")
   param QName(PackageNamespace(""), "int")
   returns QName(PackageNamespace(""), "void")
   body
    maxstack 3
    localcount 6
    initscopedepth 3
    maxscopedepth 4
    code
     getlocal0
     pushscope

     findpropstrict      QName(PackageNamespace("flash.utils"), "ByteArray")
     constructprop       QName(PackageNamespace("flash.utils"), "ByteArray"), 0
     coerce              QName(PackageNamespace("flash.utils"), "ByteArray")
     setlocal3

     getlocal3
     pushbyte            4
     callpropvoid        QName(PackageNamespace(""), "writeByte"), 1

     getlocal3
     pushbyte            9
     callpropvoid        QName(PackageNamespace(""), "writeByte"), 1

     getlocal3
     getlocal2
     callpropvoid        QName(PackageNamespace(""), "writeByte"), 1

     getlocal3
     pushbyte            1
     callpropvoid        QName(PackageNamespace(""), "writeByte"), 1

     getlex              QName(PackageNamespace(""), "Client")
     getproperty         QName(PackageNamespace(""), "recvClass")
     dup
     setlocal            5

     getlex              QName(PackageNamespace(""), "Client")
     getproperty         QName(PackageNamespace(""), "recvPacketFunction")
     getproperty         MultinameL([PrivateNamespace(null, "Client#0"), PackageNamespace(""), PrivateNamespace(null, "Client#1"), PackageInternalNs(""), Namespace("http://adobe.com/AS3/2006/builtin"), ProtectedNamespace("Client"), StaticProtectedNs("Client")])
     getlocal            5
     getlocal3
     call                1
     pop
     kill                5
     findpropstrict      QName(PackageNamespace("flash.utils"), "ByteArray")
     constructprop       QName(PackageNamespace("flash.utils"), "ByteArray"), 0
     coerce              QName(PackageNamespace("flash.utils"), "ByteArray")
     dup
     setlocal            4

     getlocal1
     callpropvoid        QName(PackageNamespace(""), "writeInt"), 1

     getlocal            4
     getlocal2
     callpropvoid        QName(PackageNamespace(""), "writeByte"), 1

     getlex              QName(PackageNamespace(""), "Client")
     getlocal            4
     callpropvoid        QName(PackageNamespace(""), "sendPacket"), 1

     returnvoid
    end ; code
   end ; body
  end ; method
 end ; trait
 trait method QName(PackageNamespace(""), "onSend") flag FINAL dispid 8
  method
   refid "Client/onSend"
   param QName(PackageNamespace("flash.utils"), "ByteArray")
   returns QName(PackageNamespace(""), "void")
   body
    maxstack 2
    localcount 4
    initscopedepth 3
    maxscopedepth 4
    code
     getlocal0
     pushscope

     getlocal1
     pushbyte            0
     setproperty         QName(PackageNamespace(""), "position")

     getlocal1
     callproperty        QName(PackageNamespace(""), "readUnsignedByte"), 0
     convert_i
     setlocal2

     getlocal1
     callproperty        QName(PackageNamespace(""), "readUnsignedByte"), 0
     convert_i
     setlocal3

     getlocal2
     pushbyte            4
     equals
     dup
     iffalse             L22

     pop
     getlocal3
     pushbyte            9
     equals
L22:
     iffalse             L30

     getlex              QName(PackageNamespace(""), "Client")
     getproperty         QName(PackageNamespace(""), "roundCode")
     pushbyte            255
     ifeq                L30

     getlex              QName(PackageNamespace(""), "Client")
     pushbyte            255
     setproperty         QName(PackageNamespace(""), "roundCode")
   
L30:
     returnvoid
    end ; code
   end ; body
  end ; method
 end ; trait
 trait method QName(PackageNamespace(""), "onMove") flag FINAL dispid 9
  method
   refid "Client/onMove"
   returns QName(PackageNamespace(""), "void")
   body
    maxstack 2
    localcount 1
    initscopedepth 3
    maxscopedepth 4
    code
     getlocal0
     pushscope

     getlex              QName(PackageNamespace(""), "Client")
     getproperty         QName(PackageNamespace(""), "roundCode")
     pushbyte            255
     ifeq                L9

     getlex              QName(PackageNamespace(""), "Client")
     pushbyte            255
     setproperty         QName(PackageNamespace(""), "roundCode")

L9:
     returnvoid
    end ; code
   end ; body
  end ; method
 end ; trait
 trait method QName(PackageNamespace(""), "onReceive") flag FINAL dispid 10
  method
   refid "Client/onReceive"
   param QName(PackageNamespace("flash.utils"), "ByteArray")
   returns QName(PackageNamespace(""), "void")
   body
    maxstack 4
    localcount 15
    initscopedepth 3
    maxscopedepth 4
    code
     getlocal0
     pushscope

     pushbyte            0
     setlocal            4

     pushbyte            0
     setlocal            5

     pushbyte            0
     setlocal            6

     pushbyte            0
     setlocal            7

     pushnull
     coerce_s
     setlocal            8

     pushbyte            0
     setlocal            9

     pushfalse
     setlocal            10
     
     pushbyte            0
     setlocal            11
     
     pushbyte            0
     setlocal            12
     
     pushnull
     coerce_s
     setlocal            13
     
     pushnull
     coerce              QName(PackageNamespace("flash.utils"), "ByteArray")
     setlocal            14

     getlocal1
     pushbyte            0
     setproperty         QName(PackageNamespace(""), "position")

     getlocal1
     callproperty        QName(PackageNamespace(""), "readUnsignedByte"), 0
     convert_i
     setlocal2

     getlocal1
     callproperty        QName(PackageNamespace(""), "readUnsignedByte"), 0
     convert_i
     setlocal3

     getlocal2
     pushbyte            5
     equals
     dup
     iffalse             L38

     pop
     getlocal3
     pushbyte            2
     equals
     
L38:
     iffalse             L41

     getlocal1
     callproperty        QName(PackageNamespace(""), "readInt"), 0
     convert_i
     setlocal            4

     getlocal1
     callproperty        QName(PackageNamespace(""), "readShort"), 0
     convert_i
     setlocal            5

     getlocal1
     callproperty        QName(PackageNamespace(""), "readByte"), 0
     convert_i
     setlocal            6

     getlocal1
     callproperty        QName(PackageNamespace(""), "readInt"), 0
     convert_i
     setlocal            7
     
     pushstring          ""
     setlocal            13
     
     getlocal            7
     iffalse             L39
     
     findpropstrict      QName(PackageNamespace("flash.utils"), "ByteArray")
     constructprop       QName(PackageNamespace("flash.utils"), "ByteArray"), 0
     coerce              QName(PackageNamespace("flash.utils"), "ByteArray")
     setlocal            14
     
     getlocal1
     getlocal            14
     pushbyte            0
     getlocal            7
     callpropvoid        QName(PackageNamespace(""), "readBytes"), 3
     
     getlocal            14
     pushstring          "zlib"
     callpropvoid        QName(PackageNamespace(""), "uncompress"), 1
     
     getlocal            14
     pushbyte            0
     setproperty         QName(PackageNamespace(""), "position")
     
     getlocal            14
     getlocal            14
     getproperty         QName(PackageNamespace(""), "length")
     callproperty        QName(PackageNamespace(""), "readUTFBytes"), 1
     coerce_s
     setlocal            13
     
L39:
     getlex              QName(PackageNamespace(""), "Client")
     getlocal            13
     setproperty         QName(PackageNamespace(""), "map_xml")
     
     getlocal1
     callproperty        QName(PackageNamespace(""), "readUTF"), 0
     coerce_s
     setlocal            8

     getlocal1
     callproperty        QName(PackageNamespace(""), "readByte"), 0
     convert_i
     setlocal            9

     getlocal1
     callproperty        QName(PackageNamespace(""), "readBoolean"), 0
     convert_b
     setlocal            10
     
     getlocal1
     callproperty        QName(PackageNamespace(""), "readShort"), 0
     convert_i
     setlocal            11
     
     getlocal1
     callproperty        QName(PackageNamespace(""), "readInt"), 0
     convert_i
     setlocal            12

     getlex              QName(PackageNamespace(""), "Client")
     getlocal            6
     setproperty         QName(PackageNamespace(""), "roundCode")

     getlex              QName(PackageNamespace(""), "Client")
     getlocal            6
     pushbyte            0
     add
     getlocal            4
     getlocal            10
     callpropvoid        QName(PackageNamespace(""), "onMap"), 3

L41:
     
     getlocal1
     pushbyte            0
     setproperty         QName(PackageNamespace(""), "position")

     returnvoid
    end ; code
   end ; body
  end ; method
 end ; trait
 trait method QName(PackageNamespace(""), "onMap") flag FINAL dispid 11
  method
   refid "Client/onMap"
   param QName(PackageNamespace(""), "int")
   param QName(PackageNamespace(""), "int")
   param QName(PackageNamespace(""), "Boolean")
   returns QName(PackageNamespace(""), "void")
   body
    maxstack 13
    localcount 20
    initscopedepth 3
    maxscopedepth 4
    code
     getlocal0
     pushscope

     pushbyte            0
     setlocal            8

     pushbyte            0
     setlocal            9

     pushfalse
     setlocal            10

     pushfalse
     setlocal            11

     pushbyte            0
     convert_u
     setlocal            12

     pushbyte            0
     convert_u
     setlocal            13

     pushbyte            0
     convert_u
     setlocal            14

     pushbyte            0
     convert_u
     setlocal            15

     pushfalse
     setlocal            16

     pushbyte            0
     setlocal            17

     pushbyte            0
     setlocal            18

     pushbyte            0
     setlocal            19

     getlex              QName(PackageNamespace(""), "Client")
     getproperty         QName(PackageNamespace(""), "autoplay")
     iftrue              L34

     returnvoid

L34:
     getlex              QName(PackageNamespace(""), "Client")
     getproperty         QName(PackageNamespace(""), "maps")
     getlocal2
     callproperty        QName(Namespace("http://adobe.com/AS3/2006/builtin"), "hasOwnProperty"), 1
     iftrue              L43

     getlex              QName(PackageNamespace(""), "Client")
     pushstring          "<J>[+] <N>This map is not in the database."
     callpropvoid        QName(PackageNamespace(""), "sendMessage"), 1

     returnvoid

L43:
     getlex              QName(PackageNamespace(""), "Client")
     getproperty         QName(PackageNamespace(""), "maps")
     getlocal2
     getproperty         MultinameL([PrivateNamespace(null, "Client#0"), PackageNamespace(""), PrivateNamespace(null, "Client#1"), PackageInternalNs(""), Namespace("http://adobe.com/AS3/2006/builtin"), ProtectedNamespace("Client"), StaticProtectedNs("Client")])
     coerce              QName(PackageNamespace("flash.utils"), "ByteArray")
     dup
     setlocal            4

     pushbyte            0
     setproperty         QName(PackageNamespace(""), "position")

     getlocal            4
     callproperty        QName(PackageNamespace(""), "readShort"), 0
     convert_i
     setlocal            5

     findpropstrict      QName(PackageNamespace(""), "int")
     getlex              QName(PackageNamespace(""), "Client")
     getproperty         QName(PackageNamespace(""), "bornPeriod")
     pushshort           1000
     multiply
     callproperty        QName(PackageNamespace(""), "int"), 1
     convert_i
     setlocal            6

     pushbyte            0
     setlocal            7

     jump                L232

L67:
     label
     findpropstrict      QName(PackageNamespace(""), "int")
     findpropstrict      QName(PackageNamespace(""), "Number")
     getlocal            4
     callproperty        QName(PackageNamespace(""), "readUTF"), 0
     callproperty        QName(PackageNamespace(""), "Number"), 1
     pushshort           1000
     multiply
     callproperty        QName(PackageNamespace(""), "int"), 1
     convert_i
     setlocal            8

     getlocal            4
     callproperty        QName(PackageNamespace(""), "readByte"), 0
     convert_i
     setlocal            9

     getlocal            7
     pushbyte            0
     ifngt               L90

     getlocal            6
     getlocal            8
     add
     convert_i
     setlocal            6

L90:
     getlocal            9
     pushbyte            0
     ifne                L209

     getlocal            4
     callproperty        QName(PackageNamespace(""), "readBoolean"), 0
     convert_b
     setlocal            10

     getlocal            4
     callproperty        QName(PackageNamespace(""), "readBoolean"), 0
     convert_b
     setlocal            11

     getlocal3
     iffalse             L117

     getlocal            10
     convert_b
     dup
     iftrue              L110

     pop
     getlocal            11
     convert_b
L110:
     iffalse             L117

     getlocal            10
     not
     setlocal            10

     getlocal            11
     not
     setlocal            11

L117:
     getlocal3
     iffalse             L124

     getlocal            4
     callproperty        QName(PackageNamespace(""), "readInt"), 0
     convert_u
     setlocal            12

     jump                L128

L124:
     getlocal            4
     callproperty        QName(PackageNamespace(""), "readUnsignedInt"), 0
     convert_u
     setlocal            12

L128:
     getlocal            4
     callproperty        QName(PackageNamespace(""), "readUnsignedInt"), 0
     convert_u
     setlocal            13

     getlocal            10
     convert_b
     dup
     iffalse             L139

     pop
     getlocal3
     convert_b
L139:
     iffalse             L145

     getlocal            4
     callproperty        QName(PackageNamespace(""), "readShort"), 0
     convert_u
     setlocal            14

     jump                L149

L145:
     getlocal            4
     callproperty        QName(PackageNamespace(""), "readUnsignedShort"), 0
     convert_u
     setlocal            14

L149:
     getlocal            4
     callproperty        QName(PackageNamespace(""), "readUnsignedShort"), 0
     convert_u
     setlocal            15

     getlocal3
     iffalse             L181

     findpropstrict      QName(PackageNamespace(""), "uint")
     pushshort           800
     findpropstrict      QName(PackageNamespace(""), "uint")
     getlocal            12
     pushshort           800
     multiply
     pushshort           2666
     divide
     callproperty        QName(PackageNamespace(""), "uint"), 1
     subtract
     pushshort           2666
     multiply
     pushshort           800
     divide
     callproperty        QName(PackageNamespace(""), "uint"), 1
     convert_u
     setlocal            12

     getlocal            14
     negate
     convert_u
     setlocal            14

     getlocal            10
     iffalse             L181

     getlocal            14
     convert_u
     setlocal            14

L181:
     getlocal            4
     callproperty        QName(PackageNamespace(""), "readBoolean"), 0
     convert_b
     setlocal            16

     getlocal            4
     callproperty        QName(PackageNamespace(""), "readByte"), 0
     convert_i
     setlocal            17

     getlocal            4
     callproperty        QName(PackageNamespace(""), "readByte"), 0
     convert_i
     setlocal            18

     findpropstrict      QName(PackageNamespace("flash.utils"), "setTimeout")
     getlex              QName(PackageNamespace(""), "Client")
     getproperty         QName(PackageNamespace(""), "move")
     getlocal            6
     getlocal1
     getlocal            10
     getlocal            11
     getlocal            12
     getlocal            13
     getlocal            14
     getlocal            15
     getlocal            16
     getlocal            17
     getlocal            18
     callpropvoid        QName(PackageNamespace("flash.utils"), "setTimeout"), 12

     jump                L231

L209:
     getlocal            9
     pushbyte            1
     ifne                L224

     getlocal            4
     callproperty        QName(PackageNamespace(""), "readByte"), 0
     convert_i
     setlocal            19

     findpropstrict      QName(PackageNamespace("flash.utils"), "setTimeout")
     getlex              QName(PackageNamespace(""), "Client")
     getproperty         QName(PackageNamespace(""), "crouch")
     getlocal            6
     getlex              QName(PackageNamespace(""), "roundCode")
     getlocal            19
     callpropvoid        QName(PackageNamespace("flash.utils"), "setTimeout"), 4

     jump                L231

L224:
     getlocal            9
     pushbyte            2
     ifne                L231

     getlocal            4
     callpropvoid        QName(PackageNamespace(""), "readByte"), 0

     getlocal            4
     callpropvoid        QName(PackageNamespace(""), "readUTF"), 0

L231:
     inclocal_i          7
L232:
     getlocal            7
     getlocal            5
     iflt                L67

     returnvoid
    end ; code
   end ; body
  end ; method
 end ; trait
 trait method QName(PackageNamespace(""), "move") flag FINAL dispid 12
  method
   refid "Client/move"
   param QName(PackageNamespace(""), "int")
   param QName(PackageNamespace(""), "Boolean")
   param QName(PackageNamespace(""), "Boolean")
   param QName(PackageNamespace(""), "uint")
   param QName(PackageNamespace(""), "uint")
   param QName(PackageNamespace(""), "uint")
   param QName(PackageNamespace(""), "uint")
   param QName(PackageNamespace(""), "Boolean")
   param QName(PackageNamespace(""), "int")
   param QName(PackageNamespace(""), "int")
   returns QName(PackageNamespace(""), "void")
   body
    maxstack 3
    localcount 14
    initscopedepth 3
    maxscopedepth 4
    code
     getlocal0
     pushscope

     pushnull
     coerce              QName(PackageNamespace("flash.utils"), "ByteArray")
     setlocal            12

     getlocal1
     getlex              QName(PackageNamespace(""), "Client")
     getproperty         QName(PackageNamespace(""), "roundCode")
     ifeq                L10

     returnvoid

L10:
     pushbyte            0
     setlocal            11

     jump                L81

L13:
     label
     findpropstrict      QName(PackageNamespace("flash.utils"), "ByteArray")
     constructprop       QName(PackageNamespace("flash.utils"), "ByteArray"), 0
     coerce              QName(PackageNamespace("flash.utils"), "ByteArray")
     dup
     setlocal            12

     pushbyte            4
     callpropvoid        QName(PackageNamespace(""), "writeByte"), 1

     getlocal            12
     pushbyte            4
     callpropvoid        QName(PackageNamespace(""), "writeByte"), 1

     getlocal            11
     pushbyte            0
     ifne                L31

     getlocal            12
     getlex              QName(PackageNamespace(""), "Client")
     getproperty         QName(PackageNamespace(""), "playerCode")
     callpropvoid        QName(PackageNamespace(""), "writeInt"), 1

L31:
     getlocal            12
     getlocal1
     callpropvoid        QName(PackageNamespace(""), "writeInt"), 1

     getlocal            12
     getlocal2
     callpropvoid        QName(PackageNamespace(""), "writeBoolean"), 1

     getlocal            12
     getlocal3
     callpropvoid        QName(PackageNamespace(""), "writeBoolean"), 1

     getlocal            12
     getlocal            4
     callpropvoid        QName(PackageNamespace(""), "writeUnsignedInt"), 1

     getlocal            12
     getlocal            5
     callpropvoid        QName(PackageNamespace(""), "writeUnsignedInt"), 1

     getlocal            12
     getlocal            6
     callpropvoid        QName(PackageNamespace(""), "writeShort"), 1

     getlocal            12
     getlocal            7
     callpropvoid        QName(PackageNamespace(""), "writeShort"), 1

     getlocal            12
     getlocal            8
     callpropvoid        QName(PackageNamespace(""), "writeBoolean"), 1

     getlocal            12
     getlocal            9
     callpropvoid        QName(PackageNamespace(""), "writeByte"), 1

     getlocal            12
     getlocal            10
     callpropvoid        QName(PackageNamespace(""), "writeByte"), 1

     getlocal            11
     pushbyte            0
     ifne                L77

     getlex              QName(PackageNamespace(""), "Client")
     getproperty         QName(PackageNamespace(""), "recvClass")
     dup
     setlocal            13

     getlex              QName(PackageNamespace(""), "Client")
     getproperty         QName(PackageNamespace(""), "recvPacketFunction")
     getproperty         MultinameL([PrivateNamespace(null, "Client#0"), PackageNamespace(""), PrivateNamespace(null, "Client#1"), PackageInternalNs(""), Namespace("http://adobe.com/AS3/2006/builtin"), ProtectedNamespace("Client"), StaticProtectedNs("Client")])
     getlocal            13
     getlocal            12
     call                1
     pop
     kill                13
     jump                L80

L77:
     getlex              QName(PackageNamespace(""), "Client")
     getlocal            12
     callpropvoid        QName(PackageNamespace(""), "sendPacket"), 1

L80:
     inclocal_i          11
L81:
     getlocal            11
     pushbyte            2
     iflt                L13

     returnvoid
    end ; code
   end ; body
  end ; method
 end ; trait
 trait method QName(PackageNamespace(""), "onCommand") flag FINAL dispid 13
  method
   refid "Client/onCommand"
   param QName(PackageNamespace(""), "Array")
   returns QName(PackageNamespace(""), "void")
   body
    maxstack 4
    localcount 2
    initscopedepth 3
    maxscopedepth 4
    code
     getlocal0
     pushscope
     
     getlocal1
     pushbyte            0
     getproperty         MultinameL([PrivateNamespace(null, "Client#0"), PackageNamespace(""), PrivateNamespace(null, "Client#1"), PackageInternalNs(""), Namespace("http://adobe.com/AS3/2006/builtin"), ProtectedNamespace("Client"), StaticProtectedNs("Client")])
     pushstring          "discord"
     ifne                L11

     getlex              QName(PackageNamespace(""), "Client")
     pushstring          "<N>Discord: <J>lucaselut#0001"
     callpropvoid        QName(PackageNamespace(""), "sendMessage3"), 1

     jump                L66

L11:
     getlocal1
     pushbyte            0
     getproperty         MultinameL([PrivateNamespace(null, "Client#0"), PackageNamespace(""), PrivateNamespace(null, "Client#1"), PackageInternalNs(""), Namespace("http://adobe.com/AS3/2006/builtin"), ProtectedNamespace("Client"), StaticProtectedNs("Client")])
     pushstring          "mapcount"
     ifne                L23

     getlex              QName(PackageNamespace(""), "Client")
     pushstring          "<N>Map count: <V>"
     getlex              QName(PackageNamespace(""), "Client")
     getproperty         QName(PackageNamespace(""), "mapCount")
     add
     callpropvoid        QName(PackageNamespace(""), "sendMessage3"), 1

     jump                L66

L23:
     getlocal1
     pushbyte            0
     getproperty         MultinameL([PrivateNamespace(null, "Client#0"), PackageNamespace(""), PrivateNamespace(null, "Client#1"), PackageInternalNs(""), Namespace("http://adobe.com/AS3/2006/builtin"), ProtectedNamespace("Client"), StaticProtectedNs("Client")])
     pushstring          "bornperiod"
     ifne                L34

     getlex              QName(PackageNamespace(""), "Client")
     findpropstrict      QName(PackageNamespace(""), "Number")
     getlocal1
     pushbyte            1
     getproperty         MultinameL([PrivateNamespace(null, "Client#0"), PackageNamespace(""), PrivateNamespace(null, "Client#1"), PackageInternalNs(""), Namespace("http://adobe.com/AS3/2006/builtin"), ProtectedNamespace("Client"), StaticProtectedNs("Client")])
     callproperty        QName(PackageNamespace(""), "Number"), 1
     setproperty         QName(PackageNamespace(""), "bornPeriod")

     getlex              QName(PackageNamespace(""), "Client")
     pushstring          "<N>New born period: <V>"
     getlex              QName(PackageNamespace(""), "Client")
     getproperty         QName(PackageNamespace(""), "bornPeriod")
     add
     pushstring          " <N>seconds."
     add
     callpropvoid        QName(PackageNamespace(""), "sendMessage3"), 1

     jump                L66

L34:
     getlocal1
     pushbyte            0
     getproperty         MultinameL([PrivateNamespace(null, "Client#0"), PackageNamespace(""), PrivateNamespace(null, "Client#1"), PackageInternalNs(""), Namespace("http://adobe.com/AS3/2006/builtin"), ProtectedNamespace("Client"), StaticProtectedNs("Client")])
     pushstring          "xml"
     ifne                L44

     getlex              QName(PackageNamespace(""), "Client")
     pushstring          "<N>XML:</N> <BL>"
     getlex              QName(PackageNamespace(""), "Client")
     getproperty         Multiname("map_xml", [PrivateNamespace(null, "Client#1"), PrivateNamespace(null, "Client#0"), PackageNamespace(""), PackageNamespace("Client"), PackageInternalNs("Client"), Namespace("http://adobe.com/AS3/2006/builtin"), PackageNamespace("flash.display"), PackageNamespace("flash.events"), PackageNamespace("flash.text"), PackageNamespace("flash.system"), PackageNamespace("flash.net"), PackageNamespace("flash.ui"), PackageNamespace("flash.utils"), ProtectedNamespace("Client"), StaticProtectedNs("Client"), StaticProtectedNs("flash.display:MovieClip"), StaticProtectedNs("flash.display:Sprite"), StaticProtectedNs("flash.display:DisplayObjectContainer"), StaticProtectedNs("flash.display:InteractiveObject"), StaticProtectedNs("flash.display:DisplayObject"), StaticProtectedNs("flash.events:EventDispatcher")])
     pushstring          "<"
     callproperty        Multiname("split", [PrivateNamespace(null, "Client#1"), PrivateNamespace(null, "Client#0"), PackageNamespace(""), PackageNamespace("Client"), PackageInternalNs("Client"), Namespace("http://adobe.com/AS3/2006/builtin"), PackageNamespace("flash.display"), PackageNamespace("flash.events"), PackageNamespace("flash.text"), PackageNamespace("flash.system"), PackageNamespace("flash.net"), PackageNamespace("flash.ui"), PackageNamespace("flash.utils"), ProtectedNamespace("Client"), StaticProtectedNs("Client"), StaticProtectedNs("flash.display:MovieClip"), StaticProtectedNs("flash.display:Sprite"), StaticProtectedNs("flash.display:DisplayObjectContainer"), StaticProtectedNs("flash.display:InteractiveObject"), StaticProtectedNs("flash.display:DisplayObject"), StaticProtectedNs("flash.events:EventDispatcher")]), 1
     pushstring          "&lt;"
     callproperty        Multiname("join", [PrivateNamespace(null, "Client#1"), PrivateNamespace(null, "Client#0"), PackageNamespace(""), PackageNamespace("Client"), PackageInternalNs("Client"), Namespace("http://adobe.com/AS3/2006/builtin"), PackageNamespace("flash.display"), PackageNamespace("flash.events"), PackageNamespace("flash.text"), PackageNamespace("flash.system"), PackageNamespace("flash.net"), PackageNamespace("flash.ui"), PackageNamespace("flash.utils"), ProtectedNamespace("Client"), StaticProtectedNs("Client"), StaticProtectedNs("flash.display:MovieClip"), StaticProtectedNs("flash.display:Sprite"), StaticProtectedNs("flash.display:DisplayObjectContainer"), StaticProtectedNs("flash.display:InteractiveObject"), StaticProtectedNs("flash.display:DisplayObject"), StaticProtectedNs("flash.events:EventDispatcher")]), 1
     add
     pushstring          "</BL>"
     add
     callpropvoid        QName(PackageNamespace(""), "sendMessage2"), 1
     
     jump                L66
     
L44:
     getlocal1
     pushbyte            0
     getproperty         MultinameL([PrivateNamespace(null, "Client#0"), PackageNamespace(""), PrivateNamespace(null, "Client#1"), PackageInternalNs(""), Namespace("http://adobe.com/AS3/2006/builtin"), ProtectedNamespace("Client"), StaticProtectedNs("Client")])
     pushstring          "autoplay"
     ifne                L66

     getlex              QName(PackageNamespace(""), "Client")
     getlex              QName(PackageNamespace(""), "Client")
     getproperty         QName(PackageNamespace(""), "autoplay")
     not
     setproperty         QName(PackageNamespace(""), "autoplay")

     getlex              QName(PackageNamespace(""), "Client")
     pushstring          "<N>Auto play mode: "
     getlex              QName(PackageNamespace(""), "Client")
     getproperty         QName(PackageNamespace(""), "autoplay")
     iffalse             L62

     pushstring          "<V>on"
     coerce_a
     
     jump                L64

L62:
     pushstring          "<R>off"
     coerce_a
L64:
     add
     callpropvoid        QName(PackageNamespace(""), "sendMessage3"), 1

L66:
     returnvoid
    end ; code
   end ; body
  end ; method
 end ; trait
 trait method QName(PackageNamespace(""), "b64decode") flag FINAL dispid 14
  method
   refid "Client/b64decode"
   param QName(PackageNamespace(""), "String")
   returns QName(PackageNamespace("flash.utils"), "ByteArray")
   body
    maxstack 128
    localcount 10
    initscopedepth 3
    maxscopedepth 4
    code
     getlocal0
     pushscope

     pushbyte            0
     setlocal            5

     pushbyte            0
     setlocal            6

     pushbyte            0
     setlocal            7

     pushbyte            0
     setlocal            8

     getlocal1
     getproperty         QName(PackageNamespace(""), "length")
     convert_i
     setlocal2

     findpropstrict      QName(PackageNamespace("flash.utils"), "ByteArray")
     constructprop       QName(PackageNamespace("flash.utils"), "ByteArray"), 0
     coerce              QName(PackageNamespace("flash.utils"), "ByteArray")
     setlocal3

     pushbyte            0
     setlocal            4

     pushbyte            255
     pushbyte            255
     pushbyte            255
     pushbyte            255
     pushbyte            255
     pushbyte            255
     pushbyte            255
     pushbyte            255
     pushbyte            255
     pushbyte            255
     pushbyte            255
     pushbyte            255
     pushbyte            255
     pushbyte            255
     pushbyte            255
     pushbyte            255
     pushbyte            255
     pushbyte            255
     pushbyte            255
     pushbyte            255
     pushbyte            255
     pushbyte            255
     pushbyte            255
     pushbyte            255
     pushbyte            255
     pushbyte            255
     pushbyte            255
     pushbyte            255
     pushbyte            255
     pushbyte            255
     pushbyte            255
     pushbyte            255
     pushbyte            255
     pushbyte            255
     pushbyte            255
     pushbyte            255
     pushbyte            255
     pushbyte            255
     pushbyte            255
     pushbyte            255
     pushbyte            255
     pushbyte            255
     pushbyte            255
     pushbyte            62
     pushbyte            255
     pushbyte            255
     pushbyte            255
     pushbyte            63
     pushbyte            52
     pushbyte            53
     pushbyte            54
     pushbyte            55
     pushbyte            56
     pushbyte            57
     pushbyte            58
     pushbyte            59
     pushbyte            60
     pushbyte            61
     pushbyte            255
     pushbyte            255
     pushbyte            255
     pushbyte            255
     pushbyte            255
     pushbyte            255
     pushbyte            255
     pushbyte            0
     pushbyte            1
     pushbyte            2
     pushbyte            3
     pushbyte            4
     pushbyte            5
     pushbyte            6
     pushbyte            7
     pushbyte            8
     pushbyte            9
     pushbyte            10
     pushbyte            11
     pushbyte            12
     pushbyte            13
     pushbyte            14
     pushbyte            15
     pushbyte            16
     pushbyte            17
     pushbyte            18
     pushbyte            19
     pushbyte            20
     pushbyte            21
     pushbyte            22
     pushbyte            23
     pushbyte            24
     pushbyte            25
     pushbyte            255
     pushbyte            255
     pushbyte            255
     pushbyte            255
     pushbyte            255
     pushbyte            255
     pushbyte            26
     pushbyte            27
     pushbyte            28
     pushbyte            29
     pushbyte            30
     pushbyte            31
     pushbyte            32
     pushbyte            33
     pushbyte            34
     pushbyte            35
     pushbyte            36
     pushbyte            37
     pushbyte            38
     pushbyte            39
     pushbyte            40
     pushbyte            41
     pushbyte            42
     pushbyte            43
     pushbyte            44
     pushbyte            45
     pushbyte            46
     pushbyte            47
     pushbyte            48
     pushbyte            49
     pushbyte            50
     pushbyte            51
     pushbyte            255
     pushbyte            255
     pushbyte            255
     pushbyte            255
     pushbyte            255
     newarray            128
     coerce              QName(PackageNamespace(""), "Array")
     setlocal            9

     jump                L312

L152:
     label
     jump                L155

L154:
     label
L155:
     getlocal            9
     getlocal1
     getlocal            4
     dup
     increment_i
     setlocal            4

     callproperty        QName(Namespace("http://adobe.com/AS3/2006/builtin"), "charCodeAt"), 1
     pushshort           255
     bitand
     getproperty         MultinameL([PrivateNamespace(null, "Client#0"), PackageNamespace(""), PrivateNamespace(null, "Client#1"), PackageInternalNs(""), Namespace("http://adobe.com/AS3/2006/builtin"), ProtectedNamespace("Client"), StaticProtectedNs("Client")])
     convert_i
     setlocal            5

     getlocal            4
     getlocal2
     lessthan
     dup
     iffalse             L176

     pop
     getlocal            5
     pushbyte            255
     equals
L176:
     iftrue              L154

     getlocal            5
     pushbyte            255
     ifne                L181

     jump                L315

L181:
     jump                L183

L182:
     label
L183:
     getlocal            9
     getlocal1
     getlocal            4
     dup
     increment_i
     setlocal            4

     callproperty        QName(Namespace("http://adobe.com/AS3/2006/builtin"), "charCodeAt"), 1
     pushshort           255
     bitand
     getproperty         MultinameL([PrivateNamespace(null, "Client#0"), PackageNamespace(""), PrivateNamespace(null, "Client#1"), PackageInternalNs(""), Namespace("http://adobe.com/AS3/2006/builtin"), ProtectedNamespace("Client"), StaticProtectedNs("Client")])
     convert_i
     setlocal            6

     getlocal            4
     getlocal2
     lessthan
     dup
     iffalse             L204

     pop
     getlocal            6
     pushbyte            255
     equals
L204:
     iftrue              L182

     getlocal            6
     pushbyte            255
     ifne                L209

     jump                L315

L209:
     getlocal3
     getlocal            5
     pushbyte            2
     lshift
     getlocal            6
     pushbyte            48
     bitand
     pushbyte            4
     rshift
     bitor
     callpropvoid        QName(PackageNamespace(""), "writeByte"), 1

     jump                L222

L221:
     label
L222:
     getlocal1
     getlocal            4
     dup
     increment_i
     setlocal            4

     callproperty        QName(Namespace("http://adobe.com/AS3/2006/builtin"), "charCodeAt"), 1
     pushshort           255
     bitand
     dup
     setlocal            7

     pushbyte            61
     ifne                L236

     getlocal3
     returnvalue

L236:
     getlocal            9
     getlocal            7
     getproperty         MultinameL([PrivateNamespace(null, "Client#0"), PackageNamespace(""), PrivateNamespace(null, "Client#1"), PackageInternalNs(""), Namespace("http://adobe.com/AS3/2006/builtin"), ProtectedNamespace("Client"), StaticProtectedNs("Client")])
     convert_i
     setlocal            7

     getlocal            4
     getlocal2
     lessthan
     dup
     iffalse             L250

     pop
     getlocal            7
     pushbyte            255
     equals
L250:
     iftrue              L221

     getlocal            7
     pushbyte            255
     ifne                L255

     jump                L315

L255:
     getlocal3
     getlocal            6
     pushbyte            15
     bitand
     pushbyte            4
     lshift
     getlocal            7
     pushbyte            60
     bitand
     pushbyte            2
     rshift
     bitor
     callpropvoid        QName(PackageNamespace(""), "writeByte"), 1

     jump                L270

L269:
     label
L270:
     getlocal1
     getlocal            4
     dup
     increment_i
     setlocal            4

     callproperty        QName(Namespace("http://adobe.com/AS3/2006/builtin"), "charCodeAt"), 1
     pushshort           255
     bitand
     dup
     setlocal            8

     pushbyte            61
     ifne                L284

     getlocal3
     returnvalue

L284:
     getlocal            9
     getlocal            8
     getproperty         MultinameL([PrivateNamespace(null, "Client#0"), PackageNamespace(""), PrivateNamespace(null, "Client#1"), PackageInternalNs(""), Namespace("http://adobe.com/AS3/2006/builtin"), ProtectedNamespace("Client"), StaticProtectedNs("Client")])
     convert_i
     setlocal            8

     getlocal            4
     getlocal2
     lessthan
     dup
     iffalse             L298

     pop
     getlocal            8
     pushbyte            255
     equals
L298:
     iftrue              L269

     getlocal            8
     pushbyte            255
     ifne                L303

     jump                L315

L303:
     getlocal3
     getlocal            7
     pushbyte            3
     bitand
     pushbyte            6
     lshift
     getlocal            8
     bitor
     callpropvoid        QName(PackageNamespace(""), "writeByte"), 1

L312:
     getlocal            4
     getlocal2
     iflt                L152

L315:
     getlocal3
     returnvalue
    end ; code
   end ; body
  end ; method
 end ; trait
 trait method QName(PackageNamespace(""), "sendMessage2") flag FINAL dispid 15
  method
   refid "Client/sendMessage2"
   param QName(PackageNamespace(""), "String")
   returns QName(PackageNamespace(""), "void")
   body
    maxstack 3
    localcount 4
    initscopedepth 3
    maxscopedepth 4
    code
     getlocal0
     pushscope

     findpropstrict      QName(PackageNamespace("flash.utils"), "ByteArray")
     constructprop       QName(PackageNamespace("flash.utils"), "ByteArray"), 0
     coerce              QName(PackageNamespace("flash.utils"), "ByteArray")
     setlocal2

     getlocal2
     pushbyte            6
     callpropvoid        QName(PackageNamespace(""), "writeByte"), 1

     getlocal2
     pushbyte            10
     callpropvoid        QName(PackageNamespace(""), "writeByte"), 1
     
     getlocal2
     pushbyte            5
     callpropvoid        QName(PackageNamespace(""), "writeByte"), 1
     
     getlocal2
     pushstring          "+"
     callpropvoid        QName(PackageNamespace(""), "writeUTF"), 1

     getlocal2
     getlocal1
     callpropvoid        QName(PackageNamespace(""), "writeUTF"), 1
     
     getlocal2
     pushbyte            0
     callpropvoid        QName(PackageNamespace(""), "writeByte"), 1
     
     getlocal2
     pushbyte            0
     callpropvoid        QName(PackageNamespace(""), "writeByte"), 1
     
     getlocal2
     pushbyte            0
     callpropvoid        QName(PackageNamespace(""), "writeByte"), 1

     getlex              QName(PackageNamespace(""), "Client")
     getproperty         QName(PackageNamespace(""), "recvClass")
     dup
     setlocal3

     getlex              QName(PackageNamespace(""), "Client")
     getproperty         QName(PackageNamespace(""), "recvPacketFunction")
     getproperty         MultinameL([PrivateNamespace(null, "Client#0"), PackageNamespace(""), PrivateNamespace(null, "Client#1"), PackageInternalNs(""), Namespace("http://adobe.com/AS3/2006/builtin"), ProtectedNamespace("Client"), StaticProtectedNs("Client")])
     getlocal3
     getlocal2
     call                1
     pop
     kill                3
     returnvoid
    end ; code
   end ; body
  end ; method
 end ; trait
 trait method QName(PackageNamespace(""), "sendMessage3") flag FINAL dispid 16
  method
   refid "Client/sendMessage3"
   param QName(PackageNamespace(""), "String")
   returns QName(PackageNamespace(""), "void")
   body
    maxstack 3
    localcount 4
    initscopedepth 3
    maxscopedepth 4
    code
     getlocal0
     pushscope

     findpropstrict      QName(PackageNamespace("flash.utils"), "ByteArray")
     constructprop       QName(PackageNamespace("flash.utils"), "ByteArray"), 0
     coerce              QName(PackageNamespace("flash.utils"), "ByteArray")
     setlocal2

     getlocal2
     pushbyte            6
     callpropvoid        QName(PackageNamespace(""), "writeByte"), 1

     getlocal2
     pushbyte            10
     callpropvoid        QName(PackageNamespace(""), "writeByte"), 1
     
     getlocal2
     pushbyte            7
     callpropvoid        QName(PackageNamespace(""), "writeByte"), 1
     
     getlocal2
     pushstring          "+"
     callpropvoid        QName(PackageNamespace(""), "writeUTF"), 1

     getlocal2
     getlocal1
     callpropvoid        QName(PackageNamespace(""), "writeUTF"), 1
     
     getlocal2
     pushbyte            0
     callpropvoid        QName(PackageNamespace(""), "writeByte"), 1
     
     getlocal2
     pushbyte            0
     callpropvoid        QName(PackageNamespace(""), "writeByte"), 1
     
     getlocal2
     pushbyte            0
     callpropvoid        QName(PackageNamespace(""), "writeByte"), 1

     getlex              QName(PackageNamespace(""), "Client")
     getproperty         QName(PackageNamespace(""), "recvClass")
     dup
     setlocal3

     getlex              QName(PackageNamespace(""), "Client")
     getproperty         QName(PackageNamespace(""), "recvPacketFunction")
     getproperty         MultinameL([PrivateNamespace(null, "Client#0"), PackageNamespace(""), PrivateNamespace(null, "Client#1"), PackageInternalNs(""), Namespace("http://adobe.com/AS3/2006/builtin"), ProtectedNamespace("Client"), StaticProtectedNs("Client")])
     getlocal3
     getlocal2
     call                1
     pop
     kill                3
     returnvoid
    end ; code
   end ; body
  end ; method
 end ; trait
end ; class
"""
script = """script ; 0
 sinit
  refid "Client.sinit"
  body
   maxstack 2
   localcount 1
   initscopedepth 1
   maxscopedepth 3
   code
    getlocal0
    pushscope

    findpropstrict      Multiname("Client", [PackageNamespace("")])
    getlex              QName(PackageNamespace(""), "Object")
    pushscope

    getlex              QName(PackageNamespace(""), "Object")
    newclass            "Client"
    popscope
    initproperty        QName(PackageNamespace(""), "Client")

    returnvoid
   end ; code
  end ; body
 end ; method
 trait class QName(PackageNamespace(""), "Client1")
  #include "Client.class.asasm"
 end ; trait
end ; script
"""
data_dec = """@echo off
cd Tools
abcexport ../tfm.swf
rabcdasm ../tfm-0.abc
"""
data2_dec = """@echo off
cd Tools
rabcasm ../tfm-0/tfm-0.main.asasm
abcreplace ../tfm.swf 0 ../tfm-0/tfm-0.main.abc
"""
import os, glob, threading, shutil, time, asyncio, json
from aiohttp import web
try:
    loop = asyncio.get_event_loop()
except:
    asyncio.set_event_loop(asyncio.new_event_loop())
    loop = asyncio.get_event_loop()
app = web.Application()

def _download_swf():
    for file in ('tfm.swf', 'tfm-0.abc'):
        if os.path.exists(file):
            os.remove(file)
    try:
        shutil.rmtree("tfm-0")
    except:
        y = 1
    import requests
    file = requests.get('https://www.transformice.com/Transformice.swf', allow_redirects=True)
    with open('tfm.swf', 'wb') as (_file):
        _file.write(file.content)
        _file.close()
    os.system("Tools\decript tfm.swf tfm.swf")
    os.system("cls")

def tryfix():
    for file in files:
        lines = ReadAllLines(file)
        x = 0
        g = 0
        d = 0
        while len(lines) > x:
            if 'Capabilities' in lines[x] and 'language' in lines[x+1] and 'Capabilities' in lines[x+2] and 'os' in lines[x+3] and 'Capabilities' in lines[x+4] and 'version' in lines[x+5]:
                x=1
                d+=1
            if d:
                if 'not' in lines[x]: g+=1
                if g == 2:
                    lines[x-2] = "     pushfalse"
                    lines[x-1] += ", remove_it"
                    lines.remove(lines[x-1])
                    break
            x+=1
        if g == 2:
            WriteAllLines(file, lines)
    return
def GetAllAsasm():
    files = []
    for asasm in glob.glob(GetPathByName("*")):
        files += [asasm]
    return glob.glob(GetPathByName("*"))
    
def GetClassNameByFile(file):
    return file.replace("\\", "/").split("/")[-1].split('.')[0].replace("%", "\\x")
    
def GetPathByName(name):
    return "./tfm-0/{0}.class.asasm".format(name.replace("\\x", "%"))
    
def ReadAllLines(path):
    return ReadAllText(path).split('\n')

def FindClass(lines, string, count):
    i = 0
    for t in lines:
        if string in t: i+=1
    return i == count
    
def ReadAllText(path):
    r = open(path.replace("\\x", "%"), encoding='utf-8')
    text = r.read()
    r.close()
    return text
    
def WriteAllLines(path, text):
    WriteAllText(path, "\n".join(map(str, text)))
    
def WriteAllText(path, text):
    w = open(path.replace("\\x", "%"), "w+")
    w.write(text)
    w.close()
    
def FindByteArray(files):
    for file in files:
        lines = ReadAllLines(file)
        if FindClass(lines,"writeUTF",2) and FindClass(lines,"writeByte",1) and FindClass(lines,"writeInt",0) and FindClass(lines,"writeShort",0):
            y = 1
        else:
            continue
        x = 0
        while x < len(lines):
            if 'callpropvoid        QName(PackageNamespace(""), "writeUTF"), 1' in lines[x]:
                if 'getlex' in lines[x+2]:
                    return lines[x+2].split('"')[3]
            x+=1
    return ''

def replaceids():
    for f in files:
        l = ReadAllLines(f)
        x = 0
        while len(l) > x:
            if 'pushstring          "Arbitre"' in l[x]:
                l[x] = '    pushstring          "Server"'
                while not '12161994' in l[x]:x+=1
                l[x] = l[x].replace('12161994','7108545')
                while not 'pushstring          "MapCrew"' in l[x]:x+=1
                l[x] = '    pushstring          "Client"'
                while not '5544158' in l[x]:x+=1
                l[x] = l[x].replace('5544158','8255999')
                WriteAllLines(f, l)
                return
            x+=1

def FindSendString(_class):
    lines = ReadAllLines(_class[1])
    x = 0
    while x < len(lines):
        if 'callpropvoid        QName(PackageNamespace(""), "writeBytes"), 1' in lines[x] and 'getproperty' in lines[x-1]:
            send = lines[x-1].split('"')[3]
            while not 'callpropvoid        QName(PackageNamespace(""), "flush"), 0' in lines[x]:
                x+=1
            lines.insert(x+1, '')
            lines.insert(x+2, '      getlex              QName(PackageNamespace(""), "Client")')
            lines.insert(x+3,'      getlocal1')
            lines.insert(x+4,f'      getproperty         QName(PackageNamespace(""), "{send}")')
            lines.insert(x+5,'      callpropvoid        QName(PackageNamespace(""), "onSend"), 1')
            WriteAllLines(_class[1], lines)
            return send
        x+=1
    return ''

def FindAllString(file):
    lines = ReadAllLines(file)
    x = 0
    while x < len(lines):
        if 'QName(PackageNamespace("flash.net"), "Socket")' in lines[x] and 'trait slot' in lines[x]:
            socket = lines[x].split('"')[3]
            i = x
            while not 'QName(PackageNamespace(""), "int")' in lines[x]:
                x-=1
            packetid = lines[x].split('"')[3]
            x = i
        if 'end ; class' in lines[x]:
            while not 'end ; method' in lines[x]:
                x-=1
            main = lines[x+1].split('"')[3]
            bulle = lines[x+2].split('"')[3]
            return [main, bulle, socket, packetid]
        x+=1

def getplayercode():
    for file in files:
        lines = ReadAllLines(file)
        x = 0
        if FindClass(lines, "readInt", 3) and FindClass(lines, "readUTF", 3) and FindClass(lines, "readByte", 3):
            y = 1
        else:
            continue
        found = 0
        while x < len(lines):
            if 'readInt' in lines[x]: found+=1
            if found == 3:
                recev=lines[x+1].split('"')[3]
                lines.insert(x+2, '')
                lines.insert(x+3, '     getlex              QName(PackageNamespace(""), "Client")')
                lines.insert(x+4,'     getlocal0')
                lines.insert(x+5,f'     getproperty         QName(PackageNamespace(""), "{recev}")')
                lines.insert(x+6,'     setproperty         QName(PackageNamespace(""), "playerCode")')
                WriteAllLines(file, lines)
                return recev

            x+=1

def getcommandclass():
    for file in files:
        lines = ReadAllLines(file)
        x = 0
        while x < len(lines):
            if 'pushstring          " "' in lines[x]:
                if 'findproperty' in lines[x-1]:
                    return lines[x-1].split('"')[3]
            x+=1

def findclassmove():
    found = ''
    for file in files:
        lines = ReadAllLines(file)
        x = 0
        while x < len(lines):
            if 'findpropstrict      QName(PackageNamespace(""), "addChild")' in lines[x] and 'getlocal0' in lines[x+1] and 'getproperty' in lines[x+2] and 'callpropvoid        QName(PackageNamespace(""), "addChild")' in lines[x+3] and 'L' in lines[x+5]:
                if 'callpropvoid' in lines[x-2] and 'getproperty' in lines[x-3] and 'getlex' in lines[x-4]:
                    found = lines[x-2].split('"')[3]
                    break
            x+=1
    if found == '': 
        return
    work = False
    for file in files:
        lines = ReadAllLines(file)
        x = 0
        while x < len(lines):
            if '' in lines[x-1] and 'getlocal            4' in lines[x] and f'callpropvoid        QName(PackageNamespace(""), "{found}")' in lines[x+1] and '' in lines[x+2]:
                lines.insert(x+2, '')
                lines.insert(x+3,'     getlex              QName(PackageNamespace(""), "Client")')
                lines.insert(x+4,'     callpropvoid        QName(PackageNamespace(""), "onMove"), 0')
                work = True
            x+=1
        if work:
            WriteAllLines(file, lines)
            return
        
def fixbrowser():
    for f in files:
        l = ReadAllLines(f)
        c,y,z = ['writeShort','writeUTF','writeInt']
        if FindClass(l,c,1) and FindClass(l,y,8) and FindClass(l,z,3):
            x,j,m = 0,0,0
            while len(l) > x:
                if y in l[x]:
                    j+=1
                    if j == 3:
                        l[x-1] = '	 pushstring          "Desktop"'
                    elif j == 6:
                        l[x-1] = '	 pushstring          "74696720697320676f6e6e61206b696c6c206d7920626f742e20736f20736164"'
                    elif j == 7:
                        l[x-1] = '	 pushstring          "A=t&SA=t&SV=t&EV=t&MP3=t&AE=t&VE=t&ACC=t&PR=t&SP=f&SB=f&DEB=f&V=LNX 32,0,0,182&M=Adobe Linux&R=1920x1080&COL=color&AR=1.0&OS=Linux&ARCH=x86&L=en&IME=t&PR32=t&PR64=t&LS=en-US&PT=Desktop&AVD=f&LFD=f&WD=f&TLS=t&ML=5.1&DP=72"'
                if z in l[x]:
                    m+=1
                    if m == 1:
                        l[x-1] = '	 pushint             8125'
                    elif m == 2:
                        l[x-1] = '	 pushint             0'
                    elif m == 3:
                        l[x-1] = '	 pushint             25175'
                x+=1
            WriteAllLines(f,l)
            return

def getspecialclass():
    for file in files:
        lines = ReadAllLines(file)
        x = 0
        while x < len(lines):
            if 'refid' in lines[x] and 'body' in lines[x+1] and 'cinit' in lines[x]:
                _tempclass = lines[x].split('"')[1].split('/')[0]
                if 'findpropstrict      QName(PackageNamespace("flash.display"), "Loader")' in lines[x+11]:
                    return _tempclass
            x+=1
def getclassee(_class2, _class3):
    for file in files:
        lines = ReadAllLines(file)
        x = 0
        _class = ''
        while x < len(lines):
            if _class != '':
                if 'findpropstrict      QName(PackageNamespace("flash.utils"), "Dictionary")' in lines[x] and 'constructprop       QName(PackageNamespace("flash.utils"), "Dictionary"), 0' in lines[x+1] and 'initproperty' in lines[x+2] and 'getlocal0' in lines[x+4] and 'constructsuper' in lines[x+5]:
                    lines.insert(x+6, '')
                    lines.insert(x+7,'     getlex              QName(PackageNamespace(""), "Client")')
                    lines.insert(x+8,f'     getlex              QName(PackageNamespace(""), "{_class}")')
                    lines.insert(x+9,'     setproperty         QName(PackageNamespace(""), "connectionClass")')
                    lines.insert(x+10, '')
                    lines.insert(x+11,'     getlex              QName(PackageNamespace(""), "Client")')
                    lines.insert(x+12,f'     getlex              QName(PackageNamespace(""), "{_class2}")')
                    lines.insert(x+13,'     setproperty         QName(PackageNamespace(""), "recvClass")')
                    lines.insert(x+14, '')
                    lines.insert(x+15, '     getlex              QName(PackageNamespace(""), "Client")')
                    lines.insert(x+16, '     callpropvoid        QName(PackageNamespace(""), "downloadMaps"), 0')
                    while x < len(lines):
                        if f'getproperty         QName(PackageNamespace(""), "{_class3}")' in lines[x]:
                            while not 'setlocal            5' in lines[x]:
                                x+=1
                            lines.insert(x, '')
                            lines.insert(x, '      getlex              QName(PackageNamespace(""), "Client")')
                            lines.insert(x+1, '      getlocal            4')
                            lines.insert(x+2,'      callpropvoid        QName(PackageNamespace(""), "onCommand"), 1')
                            WriteAllLines(file, lines)
                            return
                        x+=1
            if '11801-12801-13801-14801' in lines[x]:
                _class = lines[x-1].split('"')[3]
                x = 0
            x+=1

            
def FindRecvString(_class):
    for file in files:
        lines = ReadAllLines(file)
        x = 0
        while x < len(lines):
            if f'getproperty         QName(PackageNamespace(""), "{_class}")' in lines[x] and 'callpropvoid' in lines[x+1]:
                if '\\x' in lines[x+1] and not '#' in lines[x+1]:
                    recv = lines[x+1].split('"')[3]
                    lines.insert(x+2, '')
                    lines.insert(x+3, '      getlex              QName(PackageNamespace(""), "Client")')
                    lines.insert(x+4,'      getlocal0')
                    lines.insert(x+5,f'      getproperty         QName(PackageNamespace(""), "{_class}")')
                    lines.insert(x+6,'      callpropvoid        QName(PackageNamespace(""), "onReceive"), 1')
                    WriteAllLines(file, lines)
                    return [recv, file]
            x+=1

def savefiles(main, sec):
    WriteAllText("./tfm-0/Client.class.asasm", main)
    WriteAllText("./tfm-0/Client.script.asasm", sec)
    lines = ReadAllLines("./tfm-0/tfm-0.main.asasm")
    if '"Client.script.asasm"' in lines: return
    x = 0
    while x < len(lines):
        if '#include' in lines[x]:
            lines.insert(x,' #include "Client.script.asasm"')
            WriteAllLines("./tfm-0/tfm-0.main.asasm", lines)
            return
        x+=1
		
async def return_dat(r, x):
    i = x()
    if isinstance(i,str):
        return web.Response(body=i,content_type='text/html')
    elif isinstance(i,bytes):
        return web.Response(body=i,content_type='application/octet-stream')
    else:
        return web.Response(body=i,content_type='text/html')
		
def run_flas():
    try:
        loop = asyncio.get_event_loop()
    except:
        asyncio.set_event_loop(asyncio.new_event_loop())
        loop = asyncio.get_event_loop()
    app.add_routes(
        [
            web.get('/Transformice.swf', lambda x: return_dat(x,tfmswf1)),
            web.get('/ChargeurTransformice.swf', lambda x: return_dat(x,tfmswf2)),
            web.get('/packets', lambda x: return_dat(x,getpackets)),
            web.get('/', lambda x: return_dat(x,htmlweb)),
        ]
    )
    web.run_app(app, port=80)

def tfmswf1():
    return open('tfm.swf', 'rb').read()

def tfmswf2():
    return open('Transformice.swf', 'rb').read()

def getpackets():
    return open('packets', 'rb').read()
	
def htmlweb():
    return '<html>\n<head>\n\t<style type="text/css">  \n\t\tbody { margin:0; }  \n\t</style>\n</head>\n<body>\n<object id="swf1" classid="clsid:d27cdb6e-ae6d-11cf-96b8-444553540000" codebase="http://fpdownload.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=9,0,0,0" width="100%" height="100%" align="middle">\n<param name="allowScriptAccess" value="always" />\n<param name="movie" value="ChargeurTransformice.swf" />\n<param name="menu" value="true" />\n<param name="quality" value="high" />\n<param name="bgcolor" value="#6A7495" />\n<embed id="swf2" src="ChargeurTransformice.swf" wmode="direct" menu="true" quality="high" bgcolor="#6A7495" width="100%" height="100%" name="Transformice" align="middle" swLiveConnect="true" allowFullScreen="true" allowScriptAccess="always" type="application/x-shockwave-flash" pluginspage="http://www.macromedia.com/go/getflashplayer" />\n</object>\n</body>\n</html>'.replace('\n','').replace('\t','')


if __name__ == "__main__":
    _download_swf()
    open("dec.bat","w").write(data_dec.replace("@echo","@echo"))
    os.system("dec.bat")
    os.remove("dec.bat")
    data = {'main':'', 'bulle':'', 'socket':'', 'packetId':'', 'recvPacketFunction':''}
    files = GetAllAsasm()
    P1 = FindByteArray(files)
    tryfix()
    fixbrowser()
    replaceids()
    if P1:
        P2 = FindRecvString(P1)
        data['recvPacketFunction'] = P2[0]
        if P2:
            P3 = FindSendString(P2)
            if P3:
                P4 = FindAllString(P2[1])
                data['main'] = P4[0]
                data['bulle'] = P4[1]
                data['socket'] = P4[2]
                data['packetId'] = P4[3]
                mainscript = mainscript.replace("mainclass", data['main'])
                mainscript = mainscript.replace("bulleclass", data['bulle'])
                mainscript = mainscript.replace("socketclass", data['socket'])
                mainscript = mainscript.replace("packeteclass", data['packetId'])
                mainscript = mainscript.replace("recvpacketclass", data['recvPacketFunction'])
                script = script.replace('Client1', 'Client')
                if P4:
                    getplayercode()
                    getclassee(getspecialclass(), getcommandclass())
                    findclassmove()
                    savefiles(mainscript, script)
                    open("dec.bat","w").write(data2_dec.replace("@echo","@echo"))
                    os.system("dec.bat")
                    os.remove("dec.bat")
                    t = threading.Thread(target=run_flas)
                    t.start()
                    os.system("Adobe Transformice.swf?d="+str(int(time.time())))
                    t.join()
    print(data)
    os.system("pause")
