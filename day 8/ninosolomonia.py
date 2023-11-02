#შექმენით მეოთხე ჯგუფის წევრების სია .დაწერეთ კოდი ისე,რომ გაიგოთ ყველა სახელსა და გვარში ერთად რამდენი  ,,ი" და ,,ა"   იქნება.
goa_family = ["ako_mitaishvili,aleksandre_tordia,anri_zubashvili,beqa_giorgobiani,che_vainakh,chxitunidze_luka,dachi_vashagashvili,dato_janezashvili,dato_quparashvili,davit_grdzelishvili,demetre_kharatishvili,ekaterine_tsintsabadze,gabrieli_molodini,gigi_gabitadze,gio_abuladze,gio_kacitadze,giorgi_ioseliani,giorgi_lobjanidze,goglichadze_nini,guri_ko,helios_cato,ilia_adamia,luka,luka,lucas_vishtekaliuki,luka_kechexmadze,merab_tsitskhvaia,mirian_gelashvili,nika_baqradze,nika_datuashvili,nika_keshelava,niko_niko,nikoloz_filishvili,noe_totadze,noi_tsomaia,rati_murgulia,rostom_chagunava,saba_jmukhadze,salome_miladze,tato_chogovadze,tekla_papava,temuri_solomnishvili,tinatin_zuzadze,tsotne_kevkhishvili,tsotne_Sartania,vakhtangadze_saba,giorgi_chkhetiani,dato_tyeshelashvili,temo_labadze,maziashvili_luka,nika_bregadze,nino_solomonia"]
x_counter = 0
for family in goa_family:
  for char in family :
    if char ==  "i" and "a" :
     x_counter += 1
print(x_counter)