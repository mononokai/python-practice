function createDocumentObject(idName) {
    let docOb = document.createElement("h1");
    docOb.setAttribute("id", idName);
    return docOb;
}

class fakeDomDaddy {
    constructor(fId, fClass, fValue) {
    this.fId = fId;
    this.fClass = fClass;
    this.fValue = fValue;
    }
}
