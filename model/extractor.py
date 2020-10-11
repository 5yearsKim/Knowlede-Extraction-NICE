import torch
from torch import nn

def label_smoothe(label, smoothing=0.):
    assert smoothing > 0 and smoothing < 0.5
    bs, num_classes = label.size()

    label = label * (1 - smoothing) + smoothing / (num_classes - 1) * (1. - label)
    return label


class Extractor(nn.Module):
    def __init__(self, flow, classifier):
        super(Extractor, self).__init__()
        self.flow = flow
        self.classifier = classifier
        self.LogSoftmax = nn.LogSoftmax(dim=1)

    def forward(self, x, cond, smoothing=0., nc=1, im_size=32):
        bs, cond_dim = cond.size(0), cond.size(1)
        x = x.view(bs, -1)
        y, log_det_J = self.flow(x, cond, reverse=True) 
        if smoothing != 0.:
            cond = label_smoothe(cond, smoothing)
        y = y.view(bs, nc, im_size, im_size)
        reg = torch.square(y).view(bs, -1).mean(1)
        #converting to image format
        y = torch.sigmoid(y)
        confidence = self.LogSoftmax(self.classifier(y))
        log_ll = torch.bmm(confidence.view(bs, 1, cond_dim), cond.view(bs, cond_dim, 1)).view(bs)
        # print(log_det_J, log_ll)
        return 1* log_det_J + 10*log_ll - 10 * reg


