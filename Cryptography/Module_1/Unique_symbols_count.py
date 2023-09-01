
def countDis(str):
    # Stores all distinct characters
    file_encrypted = set(str)


    # Return the size of the set
    return len(file_encrypted)


# Driver Code
if __name__ == "__main__":
    # Given string
    file_encrypted = ''';Is9QCj@QS=(-2lDf.*KH#IgJAU%]rC`n"AF`MP7Ch>4B+ELt*A0=E]Ci*a)/
    0JnSF(f9*B-:Yl@r!3#BlbD,BOPUq+CT.u+Dbb)BQRs+B-:V*@qfRaEb0?7AM,)L8K_GY+C]83DIal3D]j+0Gp%3B@<<W+DBNA
    (C`mh5AKYDk@rHL-FE8RKBPCsi+F.mJ+D>2,AKYGnASrW3D]i\2De'u!F!,RC+D5D3AKYo'+DlBHDg-(AF)>?%C`m.rBPD%$ASl
    !rFE8RMDfm19@<Q3)BOP@aFEM#.Cj@.GDId=!Eaa'$A0?/9F`JUCGA\O3@VKXmFD5<-/g*`-+DkP4+C\n)FD,*)
    +F.mJ+CT;%+Du+>+F.mJEcYf.Afto4D/!m+F`T)V@Wcc8H#IgJ@<,p%@3B&uDIdm"FDl1BDe:,.BkM+$/g+)2D.Oi/AT)O
    (AKZ22FD,T8F<GO@F)to6F(oN)+D58'Bm"J>BOQ'q+CQC5ASkjrCLL[gAKYr1G@be;De:,5FD5T7CghF"DJ()+F=n
    \-+Cf>-An?%)/0JeT+Co%lEZet*Ci"$6/0K%J@<<V`+CT+0G%G]>+Dl72BHV#,+F.mJEZen(@WX40$:u@MDf0W1A7]d(FD,*)
    +CQC0@;[H6+C]A"Bl5&3EbT0#DII?tGp$gB+Dbb-AKYD(Ch\!5Ch4`#D/aTB+CTA6Bk&\:@;]TuH#IgJBOQ'q+EVNEF*)>
    1CER>5+EqOABHVA=@qZusF`MA6FEMV8+CT=6H#IgJ@q]e!F(HsH5p0cXDepP<@;BFq+DG^9@;Ka&FD,
    5.CisT(ATAo3AftZ.ATE&=F)Q)@+EV:*F<G7.+Cf>,ATJu&@rcL/F"AGTD]j.8@<<W6BOr<%DJs`8ARoFb+EqL5@q
    [!%BkM+$+C\n)F`V,+F_i1BD]i_-D'3J&FE8R7Ec6/4ARlp%F`]/WDfQt/F<G%(F*&O=F!,
    4?D.7<mA0?#6+EqOABHU_+Ci=D<De:,1FD,6++EV:2DJ+#A+EMHDFD,*)+D>=/BOPs)@3B)pAnGaeF_l/F+DG^9CghU'DJ()
    *BlbD1@;]Us+E_XADBNY8/g*o-G9D!@AKZ&0Bl%TtF_i1EDfTW1@;[3%F!,X;Ed8d;@<,pkF_i17DId<iA0><%+EVNEGA
    (E,+D>=/FCArrF!,17FDi:8BlbD+Ea`["/R`aCBk&b<87`ofBl%T.BOQ'q+Du+>BPD?s+C]J8+EV:.
    +EVO?Ci^_CBPCsi+DkP4+D>>&E$/h.D'3P1+CoD)DJ()*BlbD@DfTVE+C]J8+E(j7FD,6,AKYYt+D>2)+CQC/@<-!l+CT>4D
    fTr:ASuT@+CT.u+CT)&+DG^9FD,5.D/XK;+E1n4An>Io+E):2ATBCG8TZ(hF!+m6D/"'5@;
    BEsFDi:DBPD@"+EV:*F<G[=@<<W.BlnH5AKZ#3Df$V1@<3Q&CghC,Bk&90@;Kb$+CT.u+Ceht+Co2-FCf?#+EVNE@;
    ^?5AU&<.DKIKR6tL=KDIal4E,TV:BlkJ>BOu3q+Cf>,ATJu&+EV=7AKZ21ASrW&DfQt3G%G]>+CSekBln'
    -DBNk0+DYk5GALi$B4W32Dfm17DfTK%F<GXCD.Rg&Bl7Q+FD,*)+F.mJ+DYk+G9C@+AoD^$/g*`-+DGm>De:
    ,6BOr<"BkM*jF*&O=D/aE6FCB&sALnsGBOu3qAoD^$/0JhKF<G[D+D>2,AKZ,:ASbq!F!,
    ('@ruc7ASbgoGA1r-+E)CE+EV:.+E_a:Ap%o4Df0--/d_qgDfmFNAKYN%DIjr6ATE&=G@bT,/0JG@DJ*uuFEMD.FD5Z2F!1'''

    print(countDis(file_encrypted))

codecs = ["cp1252", "cp437", "utf-16be", "utf-16", "utf-8", "utf-32"]

for codec in codecs:
    with open("text.txt", "r", encoding=codec) as file:
        text = file.read()
    print(codec.rjust(12), "|", text)

