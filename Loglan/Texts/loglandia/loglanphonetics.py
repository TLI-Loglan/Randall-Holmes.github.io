from loglanpreamble import *

L("V1 <- [aeiouyAEIOUY]")

L("V2 <- [aeiouAEIOU]")

L("C1 <- [bcdfghjklmnprstvzBCDFGHJKLMNPRSTVZ]")

L("letter <- (![qwxQWX] [a-zA-Z])")

L("lowercase <- (![qwx] [a-z])")

L("uppercase <- (![QWX] [A-Z])")

L("caprule <- ([\"]? &((letter TAI0)/([z] V1)/(!(lowercase uppercase) .)) letter (&((letter TAI0)/([z] V1)/(!(lowercase uppercase) .)) (letter/juncture))* !(letter/juncture))")

L("AlienText <- (([,]? [ ]+ [\"] (![\"] .)+ [\"])/([,]? [ ]+ (![, ] !terminal .)+ ([,]? [ ]+ [y] [,]? [ ]+ (![, ] !terminal .)+)*))")

L("AlienWord <- (&caprule (([Hh] [Oo] [Ii] juncture? &([,]? [ ]+ [\"]))/([Hh] [Uu] juncture? [Ee] juncture? &([,]? [ ]+ [\"]))/([Ll] [Ii] juncture? [Ee])/([Ll] [Aa] juncture? [Oo])/([Ss] [Aa] juncture? [Oo])/([Ss] [Uu] juncture? [Ee])) AlienText)")

L("juncture <- ((([-] &letter)/[\'*]) !juncture)")

L("stress <- ([`*] !juncture)")

L("terminal <- [.:?!;]")

L("character <- (letter/juncture)")

L("continuant <- [mnlrMNLR]")

L("syllabic <- (([mM] [mM] !(juncture? [mM]))/([nN] [nN] !(juncture? [nN]))/([rR] [rR] !(juncture? [rR]))/([lL] [lL] !(juncture? [lL])))")

L("MustMono <- (([aeoAEO] [iI])/([aA] [oO]))")

L("BrokenMono <- (([aeoAEO] juncture [iI])/([aA] juncture [oO]))")

L("Mono <- (MustMono/([iI] V2)/([uU] V2))")

L("VV <- (!BrokenMono V2 juncture? V2)")

L("NextVowels <- (MustMono/(V2 &MustMono)/Mono/V2)")

L("DoubleVowel <- (([aA] juncture? [aA])/([eE] juncture? [eE])/([oO] juncture? [oO])/([iI] juncture [iI])/([uU] juncture [uU]))")

L("Vocalic <- (NextVowels/syllabic/[y])")

L("Initial <- (([Bb] [Ll])/([Bb] [Rr])/([Cc] [Kk])/([Cc] [Ll])/([Cc] [Mm])/([Cc] [Nn])/([Cc] [Pp])/([Cc] [Rr])/([Cc] [Tt])/([Dd] [Jj])/([Dd] [Rr])/([Dd] [Zz])/([Ff] [Ll])/([Ff] [Rr])/([Gg] [Ll])/([Gg] [Rr])/([Jj] [Mm])/([Kk] [Ll])/([Kk] [Rr])/([Mm] [Rr])/([Pp] [Ll])/([Pp] [Rr])/([Ss] [Kk])/([Ss] [Ll])/([Ss] [Mm])/([Ss] [Nn])/([Ss] [Pp])/([Ss] [Rr])/([Ss] [Tt])/([Ss] [Vv])/([Tt] [Cc])/([Tt] [Rr])/([Tt] [Ss])/([Vv] [Ll])/([Vv] [Rr])/([Zz] [Bb])/([Zz] [Ll])/([Zz] [Vv]))")

L("MaybeInitial <- (([Bb] juncture? [Ll])/([Bb] juncture? [Rr])/([Cc] juncture? [Kk])/([Cc] juncture? [Ll])/([Cc] juncture? [Mm])/([Cc] juncture? [Nn])/([Cc] juncture? [Pp])/([Cc] juncture? [Rr])/([Cc] juncture? [Tt])/([Dd] juncture? [Jj])/([Dd] juncture? [Rr])/([Dd] juncture? [Zz])/([Ff] juncture? [Ll])/([Ff] juncture? [Rr])/([Gg] juncture? [Ll])/([Gg] juncture? [Rr])/([Jj] juncture? [Mm])/([Kk] juncture? [Ll])/([Kk] juncture? [Rr])/([Mm] juncture? [Rr])/([Pp] juncture? [Ll])/([Pp] juncture? [Rr])/([Ss] juncture? [Kk])/([Ss] juncture? [Ll])/([Ss] juncture? [Mm])/([Ss] juncture? [Nn])/([Ss] juncture? [Pp])/([Ss] juncture? [Rr])/([Ss] juncture? [Tt])/([Ss] juncture? [Vv])/([Tt] juncture? [Cc])/([Tt] juncture? [Rr])/([Tt] juncture? [Ss])/([Vv] juncture? [Ll])/([Vv] juncture? [Rr])/([Zz] juncture? [Bb])/([Zz] juncture? [Ll])/([Zz] juncture? [Vv]))")

L("InitialConsonants <- ((!syllabic C1 &Vocalic)/(!(C1 syllabic) Initial &Vocalic)/(&Initial C1 !(C1 syllabic) Initial !syllabic &Vocalic))")

L("NoMedial2 <- (([Bb] juncture? [Bb])/([Cc] juncture? [Cc])/([Dd] juncture? [Dd])/([Ff] juncture? [Ff])/([Gg] juncture? [Gg])/([Hh] juncture? C1)/([Jj] juncture? [Jj])/([Kk] juncture? [Kk])/([Ll] juncture? [Ll])/([Mm] juncture? [Mm])/([Nn] juncture? [Nn])/([Pp] juncture? [Pp])/([Rr] juncture? [Rr])/([Ss] juncture? [Ss])/([Tt] juncture? [Tt])/([Vv] juncture? [Vv])/([Zz] juncture? [Zz])/([CJSZcjsz] juncture? [CJSZcjsz])/([Ff] juncture? [Vv])/([Kk] juncture? [Gg])/([Pp] juncture? [Bb])/([Tt] juncture? [Dd])/([FKPTfkpt] juncture? [JZjz])/([Bb] juncture? [Jj])/([Ss] juncture? [Bb]))")

L("NoMedial3 <- (([Cc] juncture? [Dd] juncture? [Zz])/([Cc] juncture? [Vv] juncture? [Ll])/([Nn] juncture? [Dd] juncture? [Jj])/([Nn] juncture? [Dd] juncture? [Zz])/([Dd] juncture? [Cc] juncture? [Mm])/([Dd] juncture? [Cc] juncture? [Tt])/([Dd] juncture? [Tt] juncture? [Ss])/([Pp] juncture? [Dd] juncture? [Zz])/([Gg] juncture? [Tt] juncture? [Ss])/([Gg] juncture? [Zz] juncture? [Bb])/([Ss] juncture? [Vv] juncture? [Ll])/([Jj] juncture? [Dd] juncture? [Jj])/([Jj] juncture? [Tt] juncture? [Cc])/([Jj] juncture? [Tt] juncture? [Ss])/([Jj] juncture? [Vv] juncture? [Rr])/([Tt] juncture? [Vv] juncture? [Ll])/([Kk] juncture? [Dd] juncture? [Zz])/([Vv] juncture? [Tt] juncture? [Ss])/([Mm] juncture? [Zz] juncture? [Bb]))")

L("SyllableA <- ((C1 V2 FinalConsonant? (!Syllable FinalConsonant)?) !syllabic)")

L("SyllableB <- (InitialConsonants? Vocalic (!Syllable FinalConsonant)? (!Syllable FinalConsonant)?)")

L("Syllable <- ((SyllableA/SyllableB) juncture?)")

L("FinalConsonant <- (!syllabic (!(!continuant C1 !Syllable continuant) !NoMedial2 !NoMedial3 C1 !(juncture? V2)))")

L("SyllableD <- (&(InitialConsonants? ([y]/DoubleVowel/BrokenMono/(&Mono V2 DoubleVowel)/(!MustMono &Mono V2 BrokenMono))) Syllable)")

L("BorrowingSyllable <- (!syllabic !SyllableD Syllable)")

L("VowelFinal <- (InitialConsonants? Vocalic juncture? !V2)")

L("SyllableC <- (&(InitialConsonants? syllabic) Syllable)")

L("SyllableY <- (&(InitialConsonants? [y]) Syllable)")

L("StressedSyllable <- ((SyllableA/SyllableB) [\'*])")

L("NameEndSyllable <- (InitialConsonants? (syllabic/(Vocalic &FinalConsonant)) FinalConsonant? FinalConsonant? !letter)")

L("maybepause <- (V1 [\'*]? [ ]+ C1)")

L("pause <- ((C1 [\'*]? [ ]+ &letter)/(letter [\'*]? [ ]+ &V1)/(letter [\'*]? [,] [ ]+ &letter))")

L("MaybePauseSyllable <- (InitialConsonants? Vocalic [\'*]? &([ ]+ &C1))")

L("connective <- ([ ]* ([Nn] [Uu] juncture? &([Uu]/[Nn]))? ([Nn] [Oo] juncture?)? V2 juncture? !V2 !([Ff] [Ii]) !([Mm] [Aa]) !([Zz] [Ii]) !(C1 juncture? C1))")

L("PreName <- ((Syllable &Syllable)* NameEndSyllable)")

L("BadPreName <- (((MaybePauseSyllable [ ]+)/(Syllable &Syllable))* NameEndSyllable)")

L("MarkedName <- (&caprule ((([Ll] !pause [Aa] juncture?)/([Hh] [Oo] !pause [Ii] juncture?)/([Cc] !pause [Ii] juncture?)/([Ll] [Ii] juncture? !pause [Uu] juncture?)/([Gg] [Aa] [Oo] juncture?)) [ ]* &C1 &caprule PreName))")

L("FalseMarked <- (&PreName (!MarkedName character)* MarkedName)")

L("NameWord <- (((&caprule MarkedName)/([,] [ ]+ !FalseMarked &caprule PreName)/(&V1 !FalseMarked &caprule PreName)/(&caprule ((([Ll] [Aa] juncture?)/([Hh] [Oo] [Ii] juncture?)/([Cc] [Ii] juncture?)/([Ll] [Ii] [Uu] juncture?)) !V1 [,]? [ ]* &caprule PreName))) (([,]? [ ]+ !FalseMarked &caprule PreName)/([,]? [ ]+ &([Cc] [Ii]) NameWord))* &(([ ]* [Cc] [Ii] predunit)/(!([ ]* Word) .)/!.))")

L("namemarker <- ((([Ll] [Aa] juncture?)/([Hh] [Oo] [Ii] juncture?)/([Cc] [Ii] juncture?)/([Ll] [Ii] juncture? [Uu] juncture?)/([Gg] [Aa] [Oo] juncture?)) !V1)")

L("badnamemarker <- (namemarker !V1 [, ]? [ ]* !PreName BadPreName)")

L("predstart1 <- (C1? (V2 juncture?)+ (&MaybeInitial C1 juncture?)* !MaybeInitial C1 juncture? C1)")

L("predstart2 <- (C1? (V2 juncture? &V2)* V2 [\'*] C1 juncture? C1)")

L("predstart2a <- (C1? (V2 juncture? &V2)* V2 C1 [\'*] C1)")

L("predstart3 <- (C1? (V2 juncture? &(V2 juncture? V2))* DoubleVowel C1 juncture? C1)")

L("predstart4 <- (C1? (V2 juncture?)+ ((&Initial InitialConsonants)/(&MaybeInitial C1 juncture Initial)) V2 juncture? V2 juncture? !character)")

L("predstart4a <- (C1? (V2 juncture?)+ ((&Initial InitialConsonants)/(&MaybeInitial C1 juncture Initial)) V2 [\'*] !Mono V2)")

L("predstart5 <- (((C1? V2 juncture? (V2 juncture? &V2)+ V2)/VV/V2) juncture? MaybeInitial V2)")

L("predstart6 <- (C1? (VV/V2) juncture? ((&Initial InitialConsonants)/(&MaybeInitial C1 juncture Initial)) V2 !character)")

L("predstart8 <- (C1? (V2 juncture?)+ (Initial/MaybeInitial/C1) syllabic)")

L("predstart9 <- (C1 VV juncture? [y])")

L("predstart10 <- (C1 V2 juncture? C1 juncture? [y])")

L("predstart11 <- (C1 V2 juncture? C1 juncture? C1 [y])")

L("predstart <- (!predstart5 (predstart1/predstart2/predstart2a/predstart3/predstart4/predstart4a/predstart6/predstart8/predstart9/predstart10/predstart11/MaybeInitial))")

L("CmapuaUnit <- ((C1 Mono juncture? V2 !([\'*] [ ]* predstart) juncture? !V1)/(C1 (VV/([Ii] [Yy])/([Uu] [Yy])) !([\'*] [ ]* predstart) juncture? !V1)/(C1 V2 !([\'*] [ ]* predstart) juncture? !V1))")

L("Cmapua <- (&caprule ((!predstart [Nn] [Oo] juncture? (VV/([Ii] [Yy])/([Uu] [Yy])) !([\'*] [ ]* predstart) juncture?)/((!predstart (VV/([Ii] [Yy])/([Uu] [Yy])) !([\'*] [ ]* predstart) juncture?)+/((!predstart V1 !([\'*] [ ]* predstart) juncture?)? (!AlienWord !NameWord !badnamemarker !predstart CmapuaUnit)+))/(!predstart V2 !([\'*] [ ]* predstart) juncture?)) !V1 !([ ]* connective))")

L("CVV <- (C1 VV ((juncture? [y] [-]? &letter)/([r] juncture? &C1)/([n] juncture? &[r])/juncture?))")

L("CVVNoHyphen <- (C1 VV juncture?)")

L("CVVHiddenStress <- (C1 &DoubleVowel V1 [-] V1 (([-]? [y] [-]? &letter)/([r] [-]? &C1)/([n] [-]? &[r])/[-]?))")

L("CVVFinalStress <- (C1 VV (([\'*] [y] [-]? &letter)/([r] [\'*] &C1)/([n] [\'*] &[r])/[\'*]))")

L("CVVNOY <- (C1 VV (([r] juncture? &C1)/([n] juncture? &[r])/juncture?))")

L("CVVNOYFinalStress <- (C1 VV (([r] [\'*] &C1)/([n] [\'*] &[r])/[\'*]))")

L("CVVNOYMedialStress <- (C1 V2 [\'*] V2 [-]?)")

L("FinalCVV <- ((CVV !character)/CVVNOYMedialStress/CVVHiddenStress)")

L("CCV <- (Initial V2 ((juncture? [y] [-]? &letter)/juncture?))")

L("CCVStressed <- (Initial V2 (([\'*] [y] [-]? &letter)/[\'*]))")

L("CCVNOY <- (Initial V2 juncture?)")

L("CCVBad <- (MaybeInitial V2 juncture?)")

L("CCVBadStressed <- (MaybeInitial V2 [\'*])")

L("FinalCCV <- ((CCV !character)/CCVStressed)")

L("CVC <- ((C1 V2 !NoMedial2 !NoMedial3 C1 ((juncture? [y] [-]? &letter)/(juncture? &C1)))/(C1 V2 juncture C1 [y] [-]? &letter))")

L("CVCStressed <- ((C1 V2 !NoMedial2 !NoMedial3 C1 (([\'*] [y] [-]? &letter)/([\'*] &letter)))/(C1 V2 [\'*] C1 [y] [-]? &letter))")

L("CVCNOY <- (C1 V2 !NoMedial2 !NoMedial3 C1 juncture? &C1)")

L("CVCBad <- (C1 V2 !NoMedial2 !NoMedial3 juncture? C1 &C1)")

L("CVCNOYStressed <- (C1 V2 !NoMedial2 !NoMedial3 C1 [\'*] &C1)")

L("CVCBadStressed <- (C1 V2 !NoMedial2 !NoMedial3 [\'*] C1 &C1)")

L("CCVCV <- (Initial V2 juncture? C1 V2 [-]?)")

L("CCVCVStressed <- (Initial V2 [\'*] C1 V2 [-]?)")

L("CCVCVBad <- (MaybeInitial V2 juncture? C1 V2 [-]?)")

L("CCVCVBadStressed <- (MaybeInitial V2 [\'*] C1 V2 [-]?)")

L("CVCCV <- ((C1 V2 juncture? Initial V2 [-]?)/(C1 V2 !NoMedial2 C1 juncture? C1 V2 [-]?))")

L("CVCCVStressed <- ((C1 V2 [\'*] Initial V2 [-]?)/(C1 V2 !NoMedial2 C1 [\'*] C1 V2 [-]?))")

L("CCVCY <- (Initial V2 juncture? C1 [y] [-]?)")

L("CVCCY <- ((C1 V2 juncture? Initial [y] [-]?)/(C1 V2 !NoMedial2 C1 juncture? C1 [y] [-]?))")

L("CCVCYStressed <- (Initial V2 [\'*] C1 [y] [-]?)")

L("CVCCYStressed <- ((C1 V2 [\'*] Initial [y] [-]?)/(C1 V2 !NoMedial2 C1 [\'*] C1 [y] [-]?))")

L("BorrowingTail1 <- (!SyllableC &StressedSyllable BorrowingSyllable (!StressedSyllable &SyllableC BorrowingSyllable)? !StressedSyllable &BorrowingSyllable VowelFinal)")

L("BorrowingTail2 <- (!SyllableC BorrowingSyllable (!StressedSyllable &SyllableC BorrowingSyllable)? !StressedSyllable &BorrowingSyllable VowelFinal (&[y]/!character))")

L("BorrowingTail3 <- (!SyllableC !StressedSyllable BorrowingSyllable (!StressedSyllable &SyllableC BorrowingSyllable)? &BorrowingSyllable InitialConsonants? Vocalic [\'*] &[y])")

L("BorrowingTail <- (BorrowingTail1/BorrowingTail2)")

L("CCVV <- ((InitialConsonants V2 juncture? V2 juncture? !character)/(InitialConsonants V2 [\'*] !Mono V2 juncture?))")

L("PreBorrowing <- (!predstart5 !CCVV !Cmapua !SyllableC (!BorrowingTail !StressedSyllable !(SyllableC SyllableC) BorrowingSyllable)* BorrowingTail)")

L("StressedPreBorrowing <- (!predstart5 !CCVV !Cmapua !SyllableC (!BorrowingTail !StressedSyllable !(SyllableC SyllableC) BorrowingSyllable)* BorrowingTail)")

L("PreBorrowing2 <- (!predstart5 !CCVV !Cmapua !SyllableC (!BorrowingTail !StressedSyllable !(SyllableC SyllableC) BorrowingSyllable)* BorrowingTail2)")

L("PreBorrowing3 <- (!predstart5 !CCVV !Cmapua !SyllableC (!BorrowingTail3 !StressedSyllable !(SyllableC SyllableC) BorrowingSyllable)* BorrowingTail3)")

L("RFinalDjifoa <- ((CCVCVBad/CVCCV/CVVNoHyphen/CCVBad/CVCBad) (&[y]/!character))")

L("RMediallyStressed <- (CCVCVBadStressed/CVCCVStressed/CVVNOYMedialStress)")

L("RFinallyStressed <- (CVVNOYFinalStress/CCVBadStressed/CVCBadStressed/CVCNOYStressed)")

L("BorrowingComplexTail <- (RMediallyStressed/(RFinallyStressed (CVVNOY/CCVBad))/RFinalDjifoa)")

L("ResolvedBorrowing <- ((!BorrowingComplexTail (CVVNOY/CCVBad/CVCBad))* BorrowingComplexTail)")

L("Borrowing <- (!ResolvedBorrowing &caprule PreBorrowing !([ ]* connective))")

L("StressedBorrowing <- (!ResolvedBorrowing &caprule StressedPreBorrowing !([ ]* &V1 Cmapua))")

L("BorrowingDjifoa <- (!ResolvedBorrowing &caprule PreBorrowing2 (([\'*] y [,] [ ]+)/(juncture? [y] [-]?)))")

L("StressedBorrowingDjifoa <- (!ResolvedBorrowing &caprule PreBorrowing3 [y] [-]? ([,] [ ]+)?)")

L("PhoneticComplexTail1 <- (!SyllableC !SyllableY &StressedSyllable Syllable (!StressedSyllable &(SyllableC/SyllableY) Syllable)? !StressedSyllable !SyllableY VowelFinal)")

L("PhoneticComplexTail2 <- (!SyllableC !SyllableY Syllable (!StressedSyllable &(SyllableC/SyllableY) Syllable)? !StressedSyllable !SyllableY VowelFinal !character)")

L("PhoneticComplexTail <- (PhoneticComplexTail1/PhoneticComplexTail2)")

L("PhoneticComplex <- (!CCVV !Cmapua !SyllableC ((StressedBorrowingDjifoa &PhoneticComplex)/(!PhoneticComplexTail !StressedSyllable !(SyllableC SyllableC) Syllable))* PhoneticComplexTail)")

L("FinalDjifoa <- ((Borrowing/StressedBorrowing/CCVCV/CVCCV/CVVNoHyphen/CCV) !character)")

L("MediallyStressed <- (CCVCVStressed/CVCCVStressed/CVVHiddenStress/CVVNOYMedialStress)")

L("FinallyStressed <- (StressedBorrowingDjifoa/CCVCYStressed/CVCCYStressed/CVVHiddenStress/CVVFinalStress/CCVStressed/CVCStressed)")

L("ComplexTail <- ((FinallyStressed ((&(C1 Mono) CVVNoHyphen)/CCV))/MediallyStressed/FinalDjifoa)")

L("PreComplex <- ((!CVVHiddenStress !ComplexTail ((StressedBorrowingDjifoa &PhoneticComplex)/BorrowingDjifoa/CVCCY/CCVCY/CVV/CCV/CVC))* ComplexTail)")

L("Complex <- (!(C1 V2 &(C1 juncture? !FinalCVV !FinalCCV PreComplex) MaybeInitial) &caprule &PreComplex PhoneticComplex !([ ]* connective))")

L("LiQuote <- (&caprule [Ll] [Ii] juncture? comma2? [\"] phoneticutterance [\"] comma2? &caprule [Ll] [Uu] juncture? !([ ]* ((&V1 Cmapua)/connective)))")

L("Word <- (NameWord/(Cmapua !([ ]* Cmapua))/Complex)")

L("SingleWord <- (((Borrowing !.)/(Complex !.)/(Word !.)/(PreName !.)/CVV/CCV/CVC) !.)")

L("phoneticutterance1 <- (NameWord/([ ]* LiQuote)/([ ]* NameWord)/([ ]* AlienWord)/([ ]* Cmapua)/([ ]* '--')/([ ]* '...')/([ ]* Borrowing ![y])/([ ]* Complex))+")

L("phoneticutterance <- (phoneticutterance1/([,] [ ]+)/terminal)+")

L("badstress <- ([\'*] [ ]* predstart)")

L("B <- (&Cmapua [Bb])")

L("C <- (&Cmapua [Cc])")

L("D <- (&Cmapua [Dd])")

L("F <- (&Cmapua [Ff])")

L("G <- (&Cmapua [Gg])")

L("H <- (&Cmapua [Hh])")

L("J <- (&Cmapua [Jj])")

L("K <- (&Cmapua [Kk])")

L("L <- (&Cmapua [Ll])")

L("M <- (&Cmapua [Mm])")

L("N <- (&Cmapua [Nn])")

L("P <- (&Cmapua [Pp])")

L("R <- (&Cmapua [Rr])")

L("S <- (&Cmapua [Ss])")

L("T <- (&Cmapua [Tt])")

L("V <- (&Cmapua [Vv])")

L("Z <- (&Cmapua [Zz])")

L("a <- ([Aa] !badstress juncture? !V1)")

L("e <- ([Ee] !badstress juncture? !V1)")

L("i <- ([Ii] !badstress juncture? !V1)")

L("o <- ([Oo] !badstress juncture? !V1)")

L("u <- ([Uu] !badstress juncture? !V1)")

L("V3 <- (juncture? V2 !badstress)")

L("AA <- ([Aa] juncture? [a] !badstress juncture? !V1)")

L("AE <- ([Aa] juncture? [e] !badstress juncture? !V1)")

L("AI <- ([Aa] [i] !badstress juncture? !(V1 V1))")

L("AO <- ([Aa] [o] !badstress juncture? !(V1 V1))")

L("AU <- ([Aa] juncture? [u] !badstress juncture? !V1)")

L("EA <- ([Ee] juncture? [a] !badstress juncture? !V1)")

L("EE <- ([Ee] juncture? [e] !badstress juncture? !V1)")

L("EI <- ([Ee] [i] !badstress juncture? !(V1 V1))")

L("EO <- ([Ee] juncture? [o] !badstress juncture? !V1)")

L("EU <- ([Ee] juncture? [u] !badstress juncture? !V1)")

L("IA <- ([Ii] juncture? [a] !badstress juncture? !(V1 V1))")

L("IE <- ([Ii] juncture? [e] !badstress juncture? !(V1 V1))")

L("II <- ([Ii] juncture? [i] !badstress juncture? !(V1 V1))")

L("IO <- ([Ii] juncture? [o] !badstress juncture? !(V1 V1))")

L("IU <- ([Ii] juncture? [u] !badstress juncture? !(V1 V1))")

L("OA <- ([Oo] juncture? [a] !badstress juncture? !V1)")

L("OE <- ([Oo] juncture? [e] !badstress juncture? !V1)")

L("OI <- ([Oo] [i] !badstress juncture? !(V1 V1))")

L("OO <- ([Oo] juncture? [o] !badstress juncture? !V1)")

L("OU <- ([Oo] juncture? [u] !badstress juncture? !V1)")

L("UA <- ([Uu] juncture? [a] !badstress juncture? !(V1 V1))")

L("UE <- ([Uu] juncture? [e] !badstress juncture? !(V1 V1))")

L("UI <- ([Uu] juncture? [i] !badstress juncture? !(V1 V1))")

L("UO <- ([Uu] juncture? [o] !badstress juncture? !(V1 V1))")

L("UU <- ([Uu] juncture? [u] !badstress juncture? !(V1 V1))")

L("IY <- ([Ii] [Yy] !badstress juncture? !V1)")

L("UY <- ([Uu] [Yy] !badstress juncture? !V1)")

L("PAUSE <- ([,] [ ]+ !(V1/connective) &caprule)")

L("comma <- ([,] [ ]+ &caprule)")

L("comma2 <- ([,]? [ ]+ &caprule)")

L("end <- (([ ]* '#' [ ]+ utterance)/([ ]+ !.)/!.)")

L("period <- (([!.:;?] (&end/([ ]+ &caprule))) (invvoc period?)?)")

L("TAI0 <- ((V1 juncture? M a)/(V1 juncture? F i)/(V1 juncture? Z i)/(&Cmapua C1 AI u?)/(&Cmapua C1 EI (u/o)?)/(Z [i] V1 !badstress juncture? !V1 (M a)?))")

L("NOI <- (N OI)")

L("A0 <- (&Cmapua (a/e/o/u/(H a)))")

L("A <- ([ ]* &Cmapua !TAI0 (N [u] &(u/(N [o])))? (N [o])? A0 NOI? !([ ]+ PANOPAUSES PAUSE) !(PANOPAUSES !PAUSE [ ,]) (PANOPAUSES ((F i)/&PAUSE))?)")

L("ANOFI <- ([ ]* (&Cmapua !TAI0 ((N [u]) &(u/(N [o])))? (N [o])? A0 NOI? PANOPAUSES?))")

L("A1 <- A")

L("ACI <- (ANOFI C i)")

L("AGE <- (ANOFI G e)")

L("CA0 <- (((N o)? ((C a)/(C e)/(C o)/(C u)/(Z e)/(C i H a))) NOI?)")

L("CA1 <- (((N u) &((C u)/(N o)))? (N o)? CA0 !([ ]+ PANOPAUSES PAUSE) !(PANOPAUSES !PAUSE [ ,]) (PANOPAUSES ((F i)/&PAUSE))?)")

L("CA1NOFI <- (((N u) &((C u)/(N o)))? (N o)? CA0 PANOPAUSES?)")

L("CA <- ([ ]* CA1)")

L("ZE2 <- ([ ]* (Z e))")

L("I <- ([ ]* !TAI0 i !([ ]+ PANOPAUSES PAUSE) !(PANOPAUSES !PAUSE [ ,]) (PANOPAUSES ((F i)/&PAUSE))?)")

L("ICA <- ([ ]* i ((H a)/CA1))")

L("ICI <- ([ ]* i CA1NOFI? C i)")

L("IGE <- ([ ]* i CA1NOFI? G e)")

L("KA0 <- ((K a)/(K e)/(K o)/(K u)/(K i H a))")

L("KOU <- ((K OU)/(M OI)/(R AU)/(S OA)/(M OU)/(C IU))")

L("KOU1 <- (((N u N o)/(N u)/(N o)) KOU)")

L("KA <- ([ ]* ((((N u) &(K u))? KA0)/((KOU1/KOU) K i)) NOI?)")

L("KI <- ([ ]* (K i) NOI?)")

L("KOU2 <- (KOU1 !KI)")

L("BadNIStress <- ((C1 V2 V2? stress (M a)? (M OA)? NI RA)/(C1 V2 stress V2 (M a)? (M OA)? NI RA))")

L("NI0 <- (!BadNIStress ((K UA)/(G IE)/(G IU)/(H IE)/(H IU)/(K UE)/(N EA)/(N IO)/(P EA)/(P IO)/(S UU)/(S UA)/(T IA)/(Z OA)/(Z OO)/(H o)/(N i)/(N e)/(T o)/(T e)/(F o)/(F e)/(V o)/(V e)/(P i)/(R e)/(R u)/(S e)/(S o)/(H i)))")

L("SA <- (!BadNIStress ((S a)/(S i)/(S u)/(IE (comma2? !IE SA)?)) NOI?)")

L("RA <- (!BadNIStress ((R a)/(R i)/(R o)))")

L("NI1 <- ((NI0 (!BadNIStress M a)? (!BadNIStress M OA NI0*)?) (comma2 !(NI RA) &NI)?)")

L("RA1 <- ((RA (!BadNIStress M a)? (!BadNIStress M OA NI0*)?) (comma2 !(NI RA) &NI)?)")

L("NI2 <- (((SA? (NI1+/RA1))/SA) NOI? (CA0 ((SA? (NI1+/RA1))/SA) NOI?)*)")

L("NI <- ([ ]* NI2 (&(M UE) Acronym (comma/&end/&period) !(C u))? (C u)?)")

L("mex <- ([ ]* NI)")

L("CI <- ([ ]* (C i))")

L("Acronym <- ([ ]* ((M UE)/TAI0/(Z V2 !V2)) ((comma &Acronym M UE)/NI1/TAI0/(Z V2 (!V2/(Z &V2))))+)")

L("TAI <- ([ ]* (TAI0/((G AO) !V2 [ ]* (PreName/Predicate/CmapuaUnit))))")

L("DA0 <- ((T AO)/(T IO)/(T UA)/(M IO)/(M IU)/(M UO)/(M UU)/(T OA)/(T OI)/(T OO)/(T OU)/(T UO)/(T UU)/(S UO)/(H u)/(B a)/(B e)/(B o)/(B u)/(D a)/(D e)/(D i)/(D o)/(D u)/(M i)/(T u)/(M u)/(T i)/(T a)/(M o))")

L("DA1 <- ((TAI0/DA0) (C i ![ ] NI0)?)")

L("DA <- ([ ]* DA1)")

L("PA0 <- ((N u !KOU)? ((G IA)/(G UA)/(P AU)/(P IA)/(P UA)/(N IA)/(N UA)/(B IU)/(F EA)/(F IA)/(F UA)/(V IA)/(V II)/(V IU)/(C OI)/(D AU)/(D II)/(D UO)/(F OI)/(F UI)/(G AU)/(H EA)/(K AU)/(K II)/(K UI)/(L IA)/(L UI)/(M IA)/(N UI)/(P EU)/(R OI)/(R UI)/(S EA)/(S IO)/(T IE)/(V a)/(V i)/(V u)/(P a)/(N a)/(F a)/(V a)/(KOU !(N OI) !KI)) (N OI)?)")

L("PANOPAUSES <- ((!PA0 NI)? (KOU2/PA0)+ ((comma2? CA0 comma2?) (KOU2/PA0)+)* ZI?)")

L("PA3 <- ([ ]* PANOPAUSES)")

L("PA <- ((!PA0 NI)? (KOU2/PA0)+ (((comma2? CA0 comma2?)/(comma2 !mod1a)) (KOU2/PA0)+)* ZI?)")

L("PA2 <- ([ ]* PA)")

L("GA <- ([ ]* (G a))")

L("PA1 <- (PA2/GA)")

L("ZI <- ((Z i)/(Z a)/(Z u))")

L("LE <- ([ ]* ((L EA)/(L EU)/(L OE)/(L EE)/(L AA)/(L e)/(L o)/(L a)))")

L("LEFORPO <- ([ ]* ((L e)/(L o)/NI2))")

L("LIO <- ([ ]* (L IO))")

L("LAU <- ([ ]* (L AU))")

L("LOU <- ([ ]* (L OU))")

L("LUA <- ([ ]* (L UA))")

L("LUO <- ([ ]* (L UO))")

L("ZEIA <- ([ ]* Z EI a)")

L("ZEIO <- ([ ]* Z EI o)")

L("LI1 <- (L i)")

L("LU1 <- (L u)")

L("LI <- (([ ]* LI1 comma2? utterance0 comma2? LU1)/([ ]* LI1 comma2? [\"] utterance0 [\"] comma2? LU1))")

L("LAO <- ([ ]* &([Ll] [Aa] [Oo] juncture?) AlienWord)")

L("LIE <- ([ ]* &([Ll] [Ii] juncture? [Ee] juncture?) AlienWord)")

L("LW <- Cmapua")

L("LIU0 <- ((L IU)/(N IU))")

L("LIU1 <- (([ ]* [Ll] [iI] juncture? [Uu] juncture? !V1 comma2? (PreName/Word) &(comma/terminal/end))/([ ]* (L II TAI)))")

L("SUE <- ([ ]* &(([Ss] [Uu] juncture? [Ee] juncture?)/([Ss] [Aa] [Oo] juncture?)) AlienWord)")

L("CUI <- ([ ]* (C UI))")

L("GA2 <- ([ ]* (G a))")

L("GE <- ([ ]* (G e))")

L("GEU <- ([ ]* ((C UE)/(G EU)))")

L("GI <- ([ ]* ((G i)/(G OI)))")

L("GO <- ([ ]* (G o))")

L("GIO <- ([ ]* (G IO))")

L("GU <- ([ ]* (G u))")

L("GUIZA <- ([ ]* (G UI) (Z a))")

L("GUIZI <- ([ ]* (G UI) (Z i))")

L("GUIZU <- ([ ]* (G UI) (Z u))")

L("GUI <- (!GUIZA !GUIZI !GUIZU ([ ]* (G UI)))")

L("GUO <- ([ ]* (G UO))")

L("GUOA <- ([ ]* (G UO Z? a))")

L("GUOE <- ([ ]* (G UO e))")

L("GUOI <- ([ ]* (G UO Z? i))")

L("GUOO <- ([ ]* (G UO o))")

L("GUOU <- ([ ]* (G UO Z? u))")

L("GUU <- ([ ]* (G UU))")

L("GUUA <- ([ ]* (G UU a))")

L("GIUO <- ([ ]* (G IU o))")

L("GUE <- ([ ]* (G UE))")

L("GUEA <- ([ ]* (G UE a))")

L("JE <- ([ ]* (J e))")

L("JUE <- ([ ]* (J UE))")

L("JIZA <- ([ ]* ((J IE)/(J AE)/(P e)/(J i)/(J a)/(N u J i)) (Z a))")

L("JIOZA <- ([ ]* ((J IO)/(J AO)) (Z a))")

L("JIZI <- ([ ]* ((J IE)/(J AE)/(P e)/(J i)/(J a)/(N u J i)) (Z i))")

L("JIOZI <- ([ ]* ((J IO)/(J AO)) (Z i))")

L("JIZU <- ([ ]* ((J IE)/(J AE)/(P e)/(J i)/(J a)/(N u J i)) (Z u))")

L("JIOZU <- ([ ]* ((J IO)/(J AO)) (Z u))")

L("JI <- (!JIZA !JIZI !JIZU ([ ]* ((J IE)/(J AE)/(P e)/(J i)/(J a)/(N u J i))))")

L("JIO <- (!JIOZA !JIOZI !JIOZU ([ ]* ((J IO)/(J AO))))")

L("DIO <- ([ ]* ((B EU)/(C AU)/(D IO)/(F OA)/(K AO)/(J UI)/(N EU)/(P OU)/(G OA)/(S AU)/(V EU)/(Z UA)/(Z UE)/(Z UI)/(Z UO)/(Z UU)))")

L("LAE <- ([ ]* ((L AE)/(L UE)))")

L("ME <- ([ ]* ((M EA)/(M e)))")

L("MEU <- ([ ]* M EU)")

L("NU0 <- ((N UO)/(F UO)/(J UO)/(N u)/(F u)/(J u))")

L("NU <- ([ ]* (NU0 !([ ]+ (NI0/RA)) (NI0/RA)? freemod?)+)")

L("PO1 <- ([ ]* ((P o)/(P u)/(Z o)))")

L("PO1A <- ([ ]* ((P OI a)/(P UI a)/(Z OI a)/(P o Z a)/(P u Z a)/(Z o Z a)))")

L("PO1E <- ([ ]* ((P OI e)/(P UI e)/(Z OI e)))")

L("PO1I <- ([ ]* ((P OI i)/(P UI i)/(Z OI i)/(P o Z i)/(P u Z i)/(Z o Z i)))")

L("PO1O <- ([ ]* ((P OI o)/(P UI o)/(Z OI o)))")

L("PO1U <- ([ ]* ((P OI u)/(P UI u)/(Z OI u)/(P o Z u)/(P u Z u)/(Z o Z u)))")

L("POSHORT1 <- ([ ]* ((P OI)/(P UI)/(Z OI)))")

L("PO <- ([ ]* PO1)")

L("POA <- ([ ]* PO1A)")

L("POE <- ([ ]* PO1E)")

L("POI <- ([ ]* PO1E)")

L("POO <- ([ ]* PO1O)")

L("POU <- ([ ]* PO1U)")

L("POSHORT <- ([ ]* POSHORT1)")

L("DIE <- ([ ]* ((D IE)/(F IE)/(K AE)/(N UE)/(R IE)))")

L("HOI <- ([ ]* ((H OI)/(L OI)/(L OA)/(S IA)/(S IE)/(S IU)))")

L("JO <- ([ ]* (NI0/RA)? (J o))")

L("KIE <- ([ ]* (K IE))")

L("KIU <- ([ ]* (K IU))")

L("KIE2 <- (([ ]* [(] (K IE))/([ ]* (K IE) [(]))")

L("KIU2 <- (([ ]* (K IU) [)])/([ ]* [)] (K IU)))")

L("SOI <- ([ ]* (S OI))")

L("UI0 <- (&Cmapua ((!([Ii] juncture? [Ee]) VV juncture?)/(B EA)/(B UO)/(C EA)/(C IA)/(C OA)/(D OU)/(F AE)/(F AO)/(F EU)/(G EA)/(K UO)/(K UU)/(R EA)/(N AO)/(N IE)/(P AE)/(P IU)/(S AA)/(S UI)/(T AA)/(T OE)/(V OI)/(Z OU)/(L OI)/(L OA)/(S IA)/(S II)/(T OE)/(S IU)/(C AO)/(C EU)/(S IE)/(S EU)))")

L("NOUI <- (([ ]* N [o] juncture? [ ]* UI0)/([ ]* UI0 NOI))")

L("UI1 <- ([ ]* (UI0+/(NI F i)))")

L("HUE <- ([ ]* (H UE))")

L("NO1 <- ([ ]* !KOU1 !NOUI (N o) !([ ]* KOU) !([ ]* (JIO/JI/JIZA/JIOZA/JIZI/JIOZI/JIZU/JIOZU)))")

L("AcronymicName <- (Acronym &(comma/period/end))")

L("DJAN <- (PreName/AcronymicName)")

L("BI <- ([ ]* (N u)? ((B IA)/(B IE)/(C IE)/(C IO)/(B IA)/(B [i])))")

L("LWPREDA <- ((H e)/(D UA)/(D UI)/(B UA)/(B UI))")

L("Predicate <- Complex")

L("PREDA <- ([ ]* &caprule (Predicate/LWPREDA/(![ ] NI RA)))")

L("guoa <- (PAUSE? (GUOA/GU) freemod?)")

L("guoe <- (PAUSE? (GUOE/GU) freemod?)")

L("guoi <- (PAUSE? (GUOI/GU) freemod?)")

L("guoo <- (PAUSE? (GUOO/GU) freemod?)")

L("guou <- (PAUSE? (GUOU/GU) freemod?)")

L("guo <- (!guoa !guoi !guou (PAUSE? (GUO/GU) freemod?))")

L("guiza <- (PAUSE? (GUIZA/GU) freemod?)")

L("guizi <- (PAUSE? (GUIZI/GU) freemod?)")

L("guizu <- (PAUSE? (GUIZU/GU) freemod?)")

L("gui <- (PAUSE? (GUI/GU) freemod?)")

L("gue <- (PAUSE? (GUE/GU) freemod?)")

L("guea <- (PAUSE? (GUEA/GU) freemod?)")

L("guu <- (PAUSE? (GUU/GU) freemod?)")

L("guua <- (PAUSE? (GUUA/GU) freemod?)")

L("giuo <- (PAUSE? (GIUO/GU) freemod?)")

L("meu <- (PAUSE? (MEU/GU) freemod?)")

L("geu <- GEU")

L("gap <- (PAUSE? GU freemod?)")

L("juelink <- (JUE freemod? (term/(PA2 freemod? gap?)))")

L("links1 <- (juelink (freemod? juelink)* gue?)")

L("links <- ((links1/(KA freemod? links freemod? KI freemod? links1)) (freemod? A1 freemod? links1)*)")

L("jelink <- (JE freemod? (term/(PA2 freemod? gap?)))")

L("linkargs1 <- (jelink freemod? (links/gue)?)")

L("linkargs <- ((linkargs1/(KA freemod? linkargs freemod? KI freemod? linkargs1)) (freemod? A1 freemod? linkargs1)*)")

L("abstractpred <- ((POA freemod? uttAx guoa?)/(POA freemod? sentence guoa?)/(POE freemod? uttAx guoe?)/(POE freemod? sentence guoe?)/(POI freemod? uttAx guoi?)/(POI freemod? sentence guoi?)/(POO freemod? uttAx guoo?)/(POO freemod? sentence guoo?)/(POU freemod? uttAx guou?)/(POU freemod? sentence guou?)/(PO freemod? uttAx guo?)/(PO freemod? sentence guo?))")

L("predunit1 <- ((SUE/(NU freemod? GE freemod? despredE (freemod? geu comma?)?)/(NU freemod? PREDA)/(comma? GE freemod? descpred (freemod? geu comma?)?)/abstractpred/(ME freemod? argument1 meu?)/PREDA) freemod?)")

L("predunit2 <- ((NO1 freemod?)* predunit1)")

L("NO2 <- (!predunit2 NO1)")

L("predunit3 <- ((predunit2 freemod? linkargs)/predunit2)")

L("predunit <- ((POSHORT freemod?)? predunit3)")

L("kekpredunit <- ((NO1 freemod?)* KA freemod? predicate freemod? KI freemod? predicate guu?)")

L("despredA <- ((predunit/kekpredunit) (freemod? CI freemod? (predunit/kekpredunit))*)")

L("despredB <- ((!PREDA CUI freemod? despredC freemod? CA freemod? despredB)/despredA)")

L("despredC <- (despredB (freemod? despredB)*)")

L("despredD <- (despredB (freemod? CA freemod? despredB)*)")

L("despredE <- (despredD (freemod? despredD)*)")

L("descpred <- ((despredE freemod? GO freemod? descpred)/despredE)")

L("sentpred <- ((despredE freemod? GO freemod? barepred)/despredE)")

L("mod1a <- (PA3 freemod? argument1 guua?)")

L("mod1 <- ((PA3 freemod? argument1 guua?)/(PA2 freemod? !barepred gap?))")

L("kekmod <- ((NO1 freemod?)* (KA freemod? modifier freemod? KI freemod? mod))")

L("mod <- (mod1/((NO1 freemod?)* mod1)/kekmod)")

L("modifier <- (mod (A1 freemod? mod)*)")

L("name <- ((PreName/AcronymicName) ((comma2? !FalseMarked PreName)/(comma2? &([Cc] [Ii]) NameWord)/(comma2? CI predunit !(comma2? (!FalseMarked PreName)))/(comma2? CI AcronymicName))* freemod?)")

L("LANAME <- ([ ]* [Ll] [Aa] juncture? comma2? name)")

L("voc <- (([ ]* [Hh] [Oo] [Ii] juncture? comma2? name)/(HOI freemod? descpred guea? (comma2 &((!FalseMarked PreName)/([Cc] [Ii] juncture? comma2 (PreName/AcronymicName))) name)?)/(HOI freemod? argument1 guua?)/([ ]* &([Hh] [Oo] [Ii] juncture?) AlienWord))")

L("descriptn <- (!LANAME ((LAU wordset1)/(LOU wordset2)/(LE freemod? ((!mex arg1a freemod?)? (PA2 freemod?)?)? mex freemod? descpred)/(LE freemod? ((!mex arg1a freemod?)? (PA2 freemod?)?)? mex freemod? arg1a)/(GE freemod? mex freemod? descpred)/(LE freemod? ((!mex arg1a freemod?)? (PA2 freemod?)?)? descpred)))")

L("abstractn <- ((LEFORPO freemod? POA freemod? uttAx guoa?)/(LEFORPO freemod? POA freemod? sentence guoa?)/(LEFORPO freemod? POE freemod? uttAx guoe?)/(LEFORPO freemod? POE freemod? sentence guoe?)/(LEFORPO freemod? POI freemod? uttAx guoi?)/(LEFORPO freemod? POI freemod? sentence guoi?)/(LEFORPO freemod? POO freemod? uttAx guoo?)/(LEFORPO freemod? POO freemod? sentence guoo?)/(LEFORPO freemod? POU freemod? uttAx guou?)/(LEFORPO freemod? POU freemod? sentence guou?)/(LEFORPO freemod? PO freemod? uttAx guo?)/(LEFORPO freemod? PO freemod? sentence guo?))")

L("arg1 <- (abstractn/(LIO freemod? descpred guea?)/(LIO freemod? argument1 guua?)/(LIO freemod? mex gap?)/(LIO stringnospaces)/LAO/LANAME/(descriptn guua? (comma2 &((!FalseMarked PreName)/([Cc] [Ii] juncture? comma2 (PreName/AcronymicName))) name)?)/LIU1/LIE/LI)")

L("arg1a <- ((DA/TAI/arg1/(GE freemod? arg1a)) freemod?)")

L("argmod1 <- ((([ ]* (N o) [ ]*)? ((JI freemod? predicate)/(JIO freemod? sentence)/(JIO freemod? uttAx)/(JI freemod? modifier)/(JI freemod? argument1)))/(([ ]* (N o) [ ]*)? (((JIZA freemod? predicate) guiza?)/((JIOZA freemod? sentence) guiza?)/((JIOZA freemod? uttAx) guiza?)/((JIZA freemod? modifier) guiza?)/(JIZA freemod? argument1 guiza?)))/(([ ]* (N o) [ ]*)? ((JIZI freemod? predicate guizi?)/(JIOZI freemod? sentence guizi?)/(JIOZI freemod? uttAx guizi?)/(JIZI freemod? modifier guizi?)/(JIZI freemod? argument1 guizi?)))/(([ ]* (N o) [ ]*)? ((JIZU freemod? predicate guizu?)/(JIOZU freemod? sentence guizu?)/(JIOZU freemod? uttAx guizu?)/(JIZU freemod? modifier guizu?)/(JIZU freemod? argument1 guizu?))))")

L("argmod <- (argmod1 (A1 freemod? argmod1)* gui?)")

L("arg2 <- (arg1a freemod? argmod*)")

L("arg3 <- (arg2/(mex freemod? arg2))")

L("indef1 <- (mex freemod? descpred)")

L("indef2 <- (indef1 guua? argmod*)")

L("indefinite <- indef2")

L("arg4 <- ((arg3/indefinite) (ZE2 freemod? (arg3/indefinite))*)")

L("arg5 <- (arg4/(KA freemod? argument1 freemod? KI freemod? argx))")

L("argx <- ((NO1 freemod?)* (LAE freemod?)* arg5)")

L("arg7 <- (argx freemod? (ACI freemod? argx)?)")

L("arg8 <- (!GE (arg7 freemod? (A1 freemod? arg7)*))")

L("argument1 <- (((arg8 freemod? AGE freemod? argument1)/arg8) (GUU freemod? argmod)*)")

L("argument <- ((NO1 freemod?)* (DIO freemod?)* argument1)")

L("argumentA <- argument")

L("argumentB <- argument")

L("argumentC <- argument")

L("argumentD <- argument")

L("argxx <- (&((NO1 freemod?)* DIO) argument)")

L("term <- (argument/modifier)")

L("modifiers <- (modifier (freemod? modifier)*)")

L("modifiersx <- ((modifier/argxx) (freemod? (modifier/argxx))*)")

L("terms <- ((modifiersx? argumentA (freemod? modifiersx)? argumentB? (freemod? modifiersx)? argumentC? (freemod? modifiersx)? argumentD?)/modifiersx)")

L("word <- (arg1a/indef2)")

L("words1 <- (word (ZEIA word)*)")

L("words2 <- (word (ZEIO word)*)")

L("wordset1 <- (words1? LUA)")

L("wordset2 <- (words2? LUO)")

L("termset1 <- (terms/(KA freemod? termset2 freemod? guu? KI freemod? termset1))")

L("termset2 <- (termset1 (guu &A1)? (A1 freemod? termset1 (guu &A1)?)*)")

L("termset <- ((terms freemod? GO freemod? barepred)/termset2)")

L("barepred <- (sentpred freemod? ((termset guu?)/(guu &termset))?)")

L("markpred <- (PA1 freemod? barepred)")

L("backpred1 <- ((NO2 freemod?)* (barepred/markpred))")

L("backpred <- (((backpred1 (ACI freemod? backpred1)+ freemod? ((termset guu?)/(guu &termset))?) ((ACI freemod? backpred)+ freemod? ((termset guu?)/(guu &termset))?)?)/backpred1)")

L("predicate2 <- (!GE (((backpred (A1 !GE freemod? backpred)+ freemod? ((termset guu?)/(guu &termset))?) ((A1 freemod? predicate2)+ freemod? ((termset guu?)/(guu &termset))?)?)/backpred))")

L("predicate1 <- ((predicate2 AGE freemod? predicate1)/predicate2)")

L("identpred <- ((NO1 freemod?)* (BI freemod? argument1 guu?))")

L("predicate <- (predicate1/identpred)")

L("subject <- ((modifiers freemod?)? ((argxx subject)/(argument (modifiersx freemod?)?)))")

L("gasent1 <- ((NO1 freemod?)* (PA1 freemod? barepred (GA2 freemod? subject)?))")

L("gasent2 <- ((NO1 freemod?)* (PA1 freemod? sentpred modifiers? (GA2 freemod? subject freemod? GIO? freemod? terms?)))")

L("gasent <- (gasent2/gasent1)")

L("statement <- (gasent/(modifiers freemod? gasent)/(subject freemod? (GIO freemod? terms)? predicate))")

L("keksent <- ((NO1 freemod?)* ((KA freemod? sentence freemod? KI freemod? uttA1)/(KA sentence freemod? KI freemod? uttA1)/(KA freemod? headterms freemod? sentence freemod? KI freemod? uttA1)))")

L("neghead <- ((NO1 freemod? gap)/(NO2 PAUSE))")

L("sen1 <- ((neghead freemod?)* ((modifiers freemod? !gasent predicate)/statement/predicate/keksent))")

L("sentence <- (sen1 (ICA freemod? sen1)*)")

L("headterms <- (terms GI)+")

L("uttAx <- (headterms freemod? sentence giuo?)")

L("HUE0 <- ([ ]* ([Hh] UE))")

L("invvoc <- (([ ]* &caprule [Hh] [Uu] juncture? [Ee] juncture? comma2? name)/(HUE freemod? descpred guea? (comma2 &((!FalseMarked PreName)/([Cc] [Ii] juncture? comma2 (PreName/AcronymicName))) name)?)/(HUE freemod? statement giuo?)/(HUE freemod? argument1 guu?)/([ ]* &([Hh] [Uu] juncture? [Ee] juncture?) AlienWord))")

L("freemod <- ((NOUI/(SOI freemod? descpred guea?)/DIE/(NO1 DIE)/(KIE comma? utterance0 comma? KIU)/(KIE2 comma? utterance0 comma? KIU2)/invvoc/voc/(comma !(!FalseMarked PreName))/JO/UI1/([ ]* '...' ([ ]* &letter)?)/([ ]* '--' ([ ]* &letter)?)) freemod?)")

L("uttA <- ((A1/mex) freemod?)")

L("uttA1 <- ((sen1/uttAx/links/linkargs/argmod/(modifiers freemod? keksent)/terms/uttA/NO1) freemod? period?)")

L("uttC <- ((neghead freemod? uttC)/uttA1)")

L("uttD <- ((sentence period? !ICI !ICA)/(uttC (ICI freemod? uttD)*))")

L("uttE <- (uttD (ICA freemod? uttD)*)")

L("uttF <- (uttE (I freemod? uttE)*)")

L("utterance0 <- (!GE ((!PAUSE freemod period? utterance0)/(!PAUSE freemod period?)/(uttF IGE utterance0)/uttF/(I freemod? uttF?)/(I freemod? period?)/(ICA freemod? uttF)) (&I utterance0)?)")

L("utterance <- (&(phoneticutterance !.) (!GE ((!PAUSE freemod period? utterance)/(!PAUSE freemod period? (&I utterance)? end)/(uttF IGE utterance)/(I freemod? period? (&I utterance)? end)/(uttF (&I utterance)? end)/(I freemod? uttF (&I utterance)? end)/(ICA freemod? uttF (&I utterance)? end))))")

if __name__ == '__main__':interface();